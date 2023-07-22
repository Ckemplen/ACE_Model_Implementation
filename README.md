# An ACE Model Python Implementation #

- [Overview](#overview)
  - [Sources](#sources)
  - [Limitations](#limitations)
  - [UX Ideas](#potential-ux)
  - [Development Goals & Test Use Cases](#development-goals-and-test-use-cases-ideas)
- [Contribute](#contribute)
  - [Core functionality for architecture](#core-functionality-for-architecture)
  - [GUI and UX](#gui-and-ux)

## Overview ##
The aim is to create a python implementation of the ACE model that is modular in nature so that LLMs / resources / capabilities can be swapped in and out. A modular design should also make it is easier for the program to implement polymorphic features, and also easier to be slotted into various forms of deployment and UI depending on the use case. This implementation uses the ACE model as the high level architecture and structure of the program, uses Langchain for more low level management of prompt engineering and interfacing with LLMs, and then will use the concepts of Resources, Capabilities and Products to abstract away the lower level functionality. The program should then think in terms of what tangible useful products it can create with the resources and capabilities that it already has or can make.

### Sources ###
Weng, Lilian. (Jun 2023). LLM-powered Autonomous Agents". Lil’Log. https://lilianweng.github.io/posts/2023-06-23-agent/.

ACE model is a creation of Dave Shapiro: https://github.com/daveshap/Benevolent_AGI

### Limitations ###
**Finite context length**: The restricted context capacity limits the inclusion of historical information, detailed instructions, API call context, and responses. The design of the system has to work with this limited communication bandwidth, while mechanisms like self-reflection to learn from past mistakes would benefit a lot from long or infinite context windows. Although vector stores and retrieval can provide access to a larger knowledge pool, their representation power is not as powerful as full attention.

**Challenges in long-term planning and task decomposition**: Planning over a lengthy history and effectively exploring the solution space remain challenging. LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.

**Reliability of natural language interface**: Current agent system relies on natural language as an interface between LLMs and external components such as memory and tools. However, the reliability of model outputs is questionable, as LLMs may make formatting errors and occasionally exhibit rebellious behavior (e.g. refuse to follow an instruction). Consequently, much of the agent demo code focuses on parsing model output.

### Potential UX ###
Providing an upfront estimate of the time commitment and outlining the steps of the process can help set user expectations and improve the user experience. Here's how this could work with the ACE model:

**Initial Assessment**: When a new task is initiated, the ACE model could make an initial assessment of the information it needs from the user and estimate how much time the user interaction will take. This could be based on the complexity of the task, the amount of information needed, and the model's previous experiences with similar tasks.

**User Interaction Plan**: The ACE model could then generate a user interaction plan, which outlines the steps of the process and estimates when user input will be needed. This plan could be presented to the user as a checklist or timeline.

**Progress Updates**: As the task progresses, the ACE model could provide updates to the user, including completed steps, upcoming steps that require user input, and any changes to the estimated timeline.

**Adaptive Planning**: The ACE model could also adapt the plan as needed based on user feedback and the progress of the task. For example, if a step takes longer than expected or if the user provides additional information that changes the scope of the task, the ACE model could update the plan and notify the user.

This approach can help make the process more transparent to the user and give them a sense of control and involvement. It also allows the ACE model to manage its tasks more effectively and efficiently, as it can plan its activities around the times when user input is expected.

Implementing this functionality would likely involve adding new capabilities to the ACE model. For example, you might add a capability for estimating user interaction time, a capability for generating a user interaction plan, and a capability for updating the plan based on progress and feedback.

### Development Goals and Test Use Cases Ideas ###

A couple of early test use cases that are unambitious in the grand scheme of things but provide a manageable first goal for the development of the model.

**Use Case 1:** CV, Personal Statement, and Cover Letter Creation

* Aspirational Layer: The aspirational layer could be seeded with principles such as accuracy, relevance, and professionalism. The values could include the presentation of the user's skills and experiences in the best possible light.

* Global Strategy Layer: The global strategy layer could be seeded with the long-term goal of creating a CV, personal statement, and cover letter that are tailored to a specific job. This layer could also be provided with information about the job, the user's qualifications, and any specific requirements for the application.

* Agent Model Layer: The agent model layer would need to be seeded with the agent's capabilities and limitations. For this task, the agent would need capabilities such as text generation, understanding job requirements, and tailoring content to specific audiences. Limitations might include the information provided by the user and the format requirements of the documents.

* Executive Function Layer: The executive function layer would be responsible for developing a plan to achieve the goal. This could include tasks such as gathering information about the job and the user's qualifications, drafting the documents, revising the documents based on feedback, and finalizing the documents.

* Cognitive Control Layer: The cognitive control layer would be responsible for managing the tasks, such as deciding which task to do next, when to switch tasks, and when to ask for feedback.

* Task Prosecution Layer: The task prosecution layer would be responsible for executing the tasks. This could involve calling on different capabilities as needed, and managing resources such as time.

**Use Case 2:** Project Documentation Creation

* Aspirational Layer: The aspirational layer could be seeded with principles such as thoroughness, clarity, and adherence to project management best practices. The values could include the successful initiation of the project and the production of high-quality documentation.

* Global Strategy Layer: The global strategy layer could be seeded with the long-term goal of creating a suite of project documentation as per those recommended by the APM. This layer could also be provided with information about the project, the project's stakeholders, and any specific requirements for the documentation.

* Agent Model Layer: The agent model layer would need to be seeded with the agent's capabilities and limitations. For this task, the agent would need capabilities such as text generation, understanding project requirements, and structuring and organizing information. Limitations might include the information provided about the project and the format requirements of the documents.

* Executive Function Layer: The executive function layer would be responsible for developing a plan to achieve the goal. This could include tasks such as gathering information about the project, drafting the documents, revising the documents based on feedback, and finalizing the documents.

* Cognitive Control Layer: The cognitive control layer would be responsible for managing the tasks, such as deciding which task to do next, when to switch tasks, and when to ask for feedback.

* Task Prosecution Layer: The task prosecution layer would be responsible for executing the tasks. This could involve calling on different capabilities as needed, and managing resources such as time.

In each case, the ACE model could assist the user by asking for necessary information, suggesting text for the documents, and providing feedback on drafts. It could also remind the user of deadlines and help keep the process on track.

## Contribute ##
Feel free to get in touch and / or make pull requests. Some ideas for areas of focus below.

### Core functionality for architecture ###
Refine the Cognitive Layer Base Class:

* Ensure the basic functionalities and structure of the CognitiveLayer base class align with the desired functionalities of all the layers.
* Define clear interfaces for communication between layers.

Implement Specific Layer Classes:

* Develop the specific functionalities of each cognitive layer (AspirationalLayer, GlobalStrategyLayer, AgentModelLayer, ExecutiveFunctionLayer, CognitiveControlLayer, and TaskProsecutionLayer).
* For each layer, implement the process_input, execute, and other necessary methods.

Develop the Capability Classes:

* Flesh out the EthicalDecisionMakingCapability class with real decision-making logic.
* Add more capabilities as required by the different layers, and ensure they adhere to the Capability class structure.

Develop the Resource Classes:

* Develop the CurrencyResource and SemanticMemoryResource classes with their specific functionalities.
* Add more resources as required by the different layers, and ensure they adhere to the Resource class structure.

Implement User Interaction Functionality:

* Develop a system for estimating user interaction time and creating a user interaction plan.
* Implement a user interface for interaction with the ACE model. This could be a CLI (command line interface) in the beginning and later develop into a GUI or a web-based interface.

Implement Multitasking and Asynchronous Operations:

* Develop a system to allow the ACE model to work on other tasks while waiting for user input. This could involve adding support for asynchronous operations or using a concurrency model like threading or multiprocessing.

Testing:

* Write unit tests for each class and method to ensure they work as expected.
* Perform integration testing to ensure the different components of the ACE model work together correctly.

Documentation:

* Document each class, method, and module with docstrings and comments.
* Write a user manual or guide for using the ACE model.

### GUI and UX ###
Design the Interface:

* Sketch out a design for the interface, keeping user experience principles in mind. It should be intuitive and easy to navigate. This step may involve creating wireframes or mockups of the interface. 

Implement the Interface:

* Choose a suitable library or framework for GUI development in Python. Tkinter, PyQt, and Kivy are popular choices, but the best one for you will depend on your specific needs.
Develop the basic structure of the interface, such as windows, menus, buttons, and text fields.

Connect the Interface to the ACE Model:

* Implement functionality to allow the user to input data through the GUI, and for the GUI to display output from the ACE model.
Ensure the GUI updates in response to changes in the ACE model (e.g., progress updates).

Test the Interface:

* Perform usability testing to ensure the interface is easy to use and intuitive. This may involve user testing, where you observe people using the interface and gather feedback on their experience.
Conduct functional testing to make sure all elements of the GUI are working correctly.

Refine the Interface:

* Based on feedback and testing, refine and improve the interface. This might involve making changes to the layout, adding new features, or improving existing ones.