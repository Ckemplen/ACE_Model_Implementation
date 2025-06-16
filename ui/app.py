from flask import Flask, request, redirect, url_for, render_template_string
import threading
import time
import signal
import atexit

from orchestration import CognitiveArchitecture

app = Flask(__name__)

# Instantiate the cognitive architecture
architecture = CognitiveArchitecture()

# Control events for background threads
stop_event = threading.Event()
arch_thread = None
resource_thread = None

# Simple in-memory list of tasks
tasks = []

# Access the currency resource from the executive function layer
currency_resource = architecture.executive_function_layer.resources.get_resource("CurrencyResource")
remaining_currency = 0.0


def run_architecture():
    """Start the cognitive architecture execution."""
    architecture.start_execution()
    stop_event.wait()
    architecture.stop_execution()


def update_resources():
    """Periodically update resource status."""
    global remaining_currency
    while not stop_event.is_set():
        if currency_resource:
            try:
                remaining_currency = currency_resource.get_remaining()
            except Exception:
                remaining_currency = 0.0
        time.sleep(5)


def start_threads():
    global arch_thread, resource_thread
    arch_thread = threading.Thread(target=run_architecture, daemon=True)
    resource_thread = threading.Thread(target=update_resources, daemon=True)
    arch_thread.start()
    resource_thread.start()


def stop_threads(*args):
    stop_event.set()
    if arch_thread:
        arch_thread.join()
    if resource_thread:
        resource_thread.join()


# Start background threads
start_threads()

@app.teardown_appcontext
def shutdown_session(exception=None):
    stop_threads()

# Ensure background threads shut down with the Flask app
atexit.register(stop_threads)
signal.signal(signal.SIGINT, stop_threads)
signal.signal(signal.SIGTERM, stop_threads)


@app.route('/tasks')
def view_tasks():
    """Display current tasks and remaining budget."""
    return render_template_string(
        """
        <h1>Current Tasks</h1>
        <ul>
        {% for t in tasks %}<li>{{t}}</li>{% endfor %}
        </ul>
        <p>Remaining currency: {{currency}}</p>
        <a href="{{ url_for('submit_task') }}">Create Task</a>
        """,
        tasks=tasks,
        currency=remaining_currency,
    )


@app.route('/submit', methods=['GET', 'POST'])
def submit_task():
    """Form to create a new task."""
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('view_tasks'))
    return render_template_string(
        """
        <h1>New Task</h1>
        <form method="post">
            <input type="text" name="task" placeholder="Task" required>
            <input type="submit" value="Add">
        </form>
        """
    )


if __name__ == '__main__':
    app.run()
