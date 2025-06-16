# An ACE Model Python Implementation #

- [Overview](#overview)
  - [Sources](#sources)
  - [Limitations](#limitations)
  - [UX Ideas](#potential-ux)
  - [Workflow Illustration](#workflow-illustration)
  - [Key Concepts](#key-concepts)
  - [Development Goals & Test Use Cases](#development-goals-and-test-use-cases-ideas)
- [Project Structure](#project-structure)
  - [Directory tree](#directory-tree)
  - [Structure description](#structure-description)

## Overview ##
The aim is to create a python implementation of the Autonomous Cognitive Entity (ACE) model that is modular in nature so that LLMs / resources / capabilities can be swapped in and out. A modular design should also make it is easier for the program to implement polymorphic features, and also easier to be slotted into various forms of deployment and UI depending on the use case. This implementation uses the ACE model as the high level architecture and structure of the program, uses Langchain for more low level management of prompt engineering and interfacing with LLMs, and then will use the concepts of Resources, Capabilities and Products to abstract away the lower level functionality. The program should then think in terms of what tangible useful products it can create with the resources and capabilities that it already has or can make.

**At this stage the project is simply a skeleton representation in python of the architecture and concepts, not a working program. There is a lot to flesh out before there is a running MVP.**

I should also caveat that I do not expect this model to be viable **yet**, the limitations of context window and API costs will throttle the throughput of data required for this to be a transformational tool. While I fully expect the cost of API calls to come down significantly, and that context window sizes will grow exponentially, we just aren't there yet - however the idea is to be fully ready to plug in these advancements once they do arrive.

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

### Workflow Illustration ###
1. **User Commission Phase**
    - User provides initial commission to the model.
    - `ExecutiveFunctionLayer` receives the commission, performs an initial assessment with input from the `AgentModelLayer` (understanding capabilities) and the `CognitiveControlLayer` (assessing task feasibility and control), and develops a high-level plan.
    - `AspirationalLayer` and `GlobalStrategyLayer` review the plan for alignment with values and strategies, respectively.
  
2. **Initial Assessment and User Interaction Plan Creation Phase**
    - `ExecutiveFunctionLayer` creates a User Interaction Plan in collaboration with the `AgentModelLayer` and the `CognitiveControlLayer`.
    - Higher layers (`AgentModelLayer`, `GlobalStrategyLayer`, `AspirationalLayer`) review and approve the plan.
    - The approved plan is then passed to the `CognitiveControlLayer` which prepares to execute the plan.

3. **Requirements Gathering Phase**
    - The `ExecutiveFunctionLayer` interacts with the user according to the User Interaction Plan to gather necessary information and requirements.
    - The information is reviewed by `AgentModelLayer` (for checking against capabilities) and `CognitiveControlLayer` (for assessing task implications and control).
    
4. **Product Building Phase**
    - Once enough information has been gathered, the `ExecutiveFunctionLayer` initiates the task execution in collaboration with the `CognitiveControlLayer`.
    - The `CognitiveControlLayer` selects the task and delegates the actual execution to the `TaskProsecutionLayer`.
    - The `TaskProsecutionLayer` focuses on one task at a time, executing the task and detecting success or failure.
    - The product building phase is monitored by all layers. Each layer can intervene and make decisions based on its area of concern.

5. **Iteration and Feedback Phase**
    - During product building, the `ExecutiveFunctionLayer` checks in with the user to provide updates and gather feedback, with input from `AgentModelLayer` and `CognitiveControlLayer`.
    - The feedback is passed up through the layers, and each layer responds based on its area of concern.
    - The `CognitiveControlLayer` uses the feedback to decide when to switch tasks, with input from `ExecutiveFunctionLayer` and `AgentModelLayer`.

6. **Final Review and Sign Off Phase**
    - Once the product is built, the `ExecutiveFunctionLayer` presents the final suite of products to the user for review, with input from `AgentModelLayer` and `CognitiveControlLayer`.
    - The user provides final feedback, which is passed up through the layers.
    - `AspirationalLayer` and `GlobalStrategyLayer` review the final products for alignment with values and strategies, respectively.
    - If the feedback is positive and the user signs off on the product, the commission is considered complete. If the user has additional feedback or changes, the model goes back to the Iteration and Feedback Phase.


### Key concepts ###

#### The ACE Model ####
The ACE model is inspired by the OSI model to present layers of abstraction by which you can think about artificial
cognitive architectures. The primary purpose of the ACE model is to provide a framework for thinking about
autonomous, agentic systems.

Layers:

1) Aspirational Layer: Mission, values, purpose, ethics, vision, morals
2) Global Strategy: Long term thinking, context, like a CEO
3) Agent Model: (Self) Capabilities, configuration, learning
4) Executive Function: Planning, forecasting, directives, resources
5) Cognitive Control: Task switching & selection, frustration, damping
6) Task Prosecution: One task at a time, detect success & failure

#### Resources ####
Covers various tangible and intangible resources, primarily consumption of knowledge and consumption of currency, 
but also potentially consumption of cloud resources if it fits the use case.

Example: CurrencyResource tracks the amount of USD assigned to the layer to spend on LLM API calls, other API costs etc.

Example: SemanticMemoryResource would provide a knowledge base of various topics and facts of relevance.

Example: WorldStatesRssFeedsResource provides knowledge of up-to-date news from RSS feeds.

The resources, capabilities and products concepts are not technically intended to be a hierarchy, although arguably
resources would sit at the bottom of the hierarchy as a base input that is consumed by higher levels. A principle of 
the implementation is that consumption of resources should be explicitly documented and reported to the user, the 
Resource entities therefore are intended to do a lot of the legwork on documenting consumption.

#### Capabilities ####
Covers abstraction and encapsulation of various workflows that can take an action, using or creating resources if necessary.

Example: InitialAssessmentCapability would cover the various work needed to gather requirements to be used for 
creating a UserInteractionPlan product.

Example: MermaidGanttChartCapability would be able to generate gantt charts for use in products, drawing on other 
resources or products to inform what is needed.

Resources are unlikely to use capabilities, but Capabilities are likely to consume and create new resources, 
Capabilities are also the only entity able to create Products.

#### Products ####
Products encapsulate and abstract the logic for combining Resources and Capabilities to produce tangible useful 
outputs of the program.

Example: as part of professional project management, during the project initiation phase various products would be 
produced, such as BusinessCaseProduct, BudgetProposalProduct, ProjectCharterProduct etc etc.

Example: a finished word doc containing a CV created by the model, or a research report, or another professional doc.

Example: a Word doc / PDF / Powerpoint etc combining prose and charts etc. 

The key idea is Products should be things of real world value to the user that involve a multi-step process that the 
user would otherwise have to work on themselves. They bring together existing Capabilities and Resources of the model 
and serve to indicate whether there is a need for dynamically created new classes based on the user need.

#### How resources, capabilities and products (RCPs) fit into the overall program workflow ####
1. **User Commission Phase**
    - User provides initial commission to the model.
    - `CurrencyResource` is used to budget for the incoming task.
    - `ExecutiveFunctionLayer` performs an initial assessment using `InitialAssessmentCapability`.
    - `AgentModelLayer` reviews the initial assessment and identifies if any new Resources, Capabilities, and Products (RCPs) are needed to complete the task.

2. **Initial Assessment and User Interaction Plan Creation Phase**
    - `ExecutiveFunctionLayer` creates a User Interaction Plan with the help of `AgentModelLayer` and `CognitiveControlLayer`.
    - During this phase, if a need for a new resource, capability, or product is identified, it's created dynamically and integrated into the model.
    - New RCPs are reviewed and approved by the higher layers (`GlobalStrategyLayer`, `AspirationalLayer`).

3. **Requirements Gathering Phase**
    - The `ExecutiveFunctionLayer` interacts with the user according to the User Interaction Plan to gather necessary information and requirements.
    - If during this interaction it becomes apparent that a new capability or resource is needed, it's created dynamically.
    - New RCPs are again reviewed and approved by the higher layers.

4. **Product Building Phase**
    - Once enough information has been gathered, the `ExecutiveFunctionLayer` initiates the task execution in collaboration with the `CognitiveControlLayer`.
    - If a new product type is required to meet the user's needs, it's created dynamically during this phase.
    - New RCPs are reviewed and approved by the higher layers.

5. **Iteration and Feedback Phase**
    - During product building, the `ExecutiveFunctionLayer` checks in with the user to provide updates and gather feedback.
    - Feedback may lead to creating more resources or adjusting the capabilities used in the product building, which are again reviewed and approved by the higher layers.

6. **Final Review and Sign Off Phase**
    - Once the product is built, the `ExecutiveFunctionLayer` presents the final suite of products to the user for review.
    - The user provides final feedback, which is passed up through the layers.
    - Based on the feedback, the model might need to adjust resources, use different capabilities, create new versions of the products, or even create new RCPs, which would again be reviewed and approved by the higher layers.



### Development Goals and Test Use Cases Ideas ###

A couple of early test use cases that are unambitious in the grand scheme of things but provide a manageable first goal for the development of the model. The ultimate end goal is to create Autonomous Cognitive Entities that can be commissioned to take on ever greater and more complicated missions, and be trusted with the resources and capabilities required to pull these off. My view is that in the interim these ACE models should pursue lower level commissions to enable more realistic / achievable / bite-sized development goals, and to build experience and confidence over time to be entrusted with increasingly important commissions along with the commensurate increased resources and capabilities.  

The early test cases suggested below both fit into the category of well understood/defined problems with well understood/defined solutions. The ACE model should prove it is capable of dealing with these kind of commissions before moving onto test-cases where either the problem is understood but the solution is not, or where both the problem and the solution are not understood. These 3 levels represent three steps up in terms of ambiguity and complexity, and require increasingly more effective use/creation of resources and capabilites - all while also justifying increased focus on alignnment and ethical oversight.

**Test Case 1:** CV, Personal Statement, and Cover Letter Creation (Very basic 3 product job, _should_ be easy for a rudimentary ACE model to achieve)

* Aspirational Layer: The aspirational layer could be seeded with principles such as accuracy, relevance, and professionalism. The values could include the presentation of the user's skills and experiences in the best possible light.

* Global Strategy Layer: The global strategy layer could be seeded with the long-term goal of creating a CV, personal statement, and cover letter that are tailored to a specific job. This layer could also be provided with information about the job, the user's qualifications, and any specific requirements for the application.

* Agent Model Layer: The agent model layer would need to be seeded with the agent's capabilities and limitations. For this task, the agent would need capabilities such as text generation, understanding job requirements, and tailoring content to specific audiences. Limitations might include the information provided by the user and the format requirements of the documents.

* Executive Function Layer: The executive function layer would be responsible for developing a plan to achieve the goal. This could include tasks such as gathering information about the job and the user's qualifications, drafting the documents, revising the documents based on feedback, and finalizing the documents.

* Cognitive Control Layer: The cognitive control layer would be responsible for managing the tasks, such as deciding which task to do next, when to switch tasks, and when to ask for feedback.

* Task Prosecution Layer: The task prosecution layer would be responsible for executing the tasks. This could involve calling on different capabilities as needed, and managing resources such as time.

**Test Case 2:** Project Documentation Creation (More challenging, outputs of appox. 12 professional grade products, still a well-defined problem with a well-defined expected solution. )

* Aspirational Layer: The aspirational layer could be seeded with principles such as thoroughness, clarity, and adherence to project management best practices. The values could include the successful initiation of the project and the production of high-quality documentation.

* Global Strategy Layer: The global strategy layer could be seeded with the long-term goal of creating a suite of project documentation as per those recommended by the APM. This layer could also be provided with information about the project, the project's stakeholders, and any specific requirements for the documentation.

* Agent Model Layer: The agent model layer would need to be seeded with the agent's capabilities and limitations. For this task, the agent would need capabilities such as text generation, understanding project requirements, and structuring and organizing information. Limitations might include the information provided about the project and the format requirements of the documents.

* Executive Function Layer: The executive function layer would be responsible for developing a plan to achieve the goal. This could include tasks such as gathering information about the project, drafting the documents, revising the documents based on feedback, and finalizing the documents.

* Cognitive Control Layer: The cognitive control layer would be responsible for managing the tasks, such as deciding which task to do next, when to switch tasks, and when to ask for feedback.

* Task Prosecution Layer: The task prosecution layer would be responsible for executing the tasks. This could involve calling on different capabilities as needed, and managing resources such as time.

In each case, the ACE model could assist the user by asking for necessary information, suggesting text for the documents, and providing feedback on drafts. It could also remind the user of deadlines and help keep the process on track.

## Project Structure ##
### Directory Tree ###
- `ACE_Model_Implementation`
    - `README.md`
    - `requirements.txt`
    - `example.env`
    - `LICENSE`
    - `.gitignore`
    - `config.ini`
    - `resource_manager`
        - `__init__.py`
        - `ResourceManager.py`
        - `Resource.py`
        - `dynamically_created_resources`
            - `__init__.py`
        - `built_in_resources`
            - `CurrencyResource.py`
            - `SemanticMemoryResource.py`
            - `UserInteractionPlanResource.py`
            - `WorldStateRssFeedsResource.py`
            - `__init__.py`
    - `orchestration`
        - `__init__.py`
        - `CognitiveArchitecture.py`
        - `test_orchestration.py`
        - `LayerHierarchy.py`
    - `product_manager`
        - `__init__.py`
        - `ProductManager.py`
        - `Product.py`
        - `dynamically_created_products`
            - `__init__.py`
        - `built_in_products`
            - `StakeholderAnalysisProduct.py`
            - `BudgetProposalProduct.py`
            - `ResourcePlanProduct.py`
            - `BusinessCaseProduct.py`
            - `ProjectCharterProduct.py`
            - `ProjectApprovalDocumentationProduct.py`
            - `ProcurementStrategyProduct.py`
            - `__init__.py`
            - `ProjectScopeStatementProduct.py`
            - `CommunicationPlanProduct.py`
            - `LegalRegulatoryReviewProduct.py`
            - `ProjectOrganisationChartProduct.py`
            - `QualityManagementPlanProduct.py`
            - `RiskManagementPlanProduct.py`
            - `ProjectScheduleProduct.py`
    - `capability_manager`
        - `__init__.py`
        - `Capability.py`
        - `CapabilityManager.py`
        - `test_capabilities.py`
        - `dynamically_created_capabilities`
            - `__init__.py`
        - `built_in_capabilities`
            - `MermaidGanttChartCapability.py`
            - `GenerateUserInteractionPlanCapability.py`
            - `EthicalDecisionMakingCapability.py`
            - `GoogleSearchScrapeResearchCapability.py`
            - `UpdateUserInteractionPlanCapability.py`
            - `InitialAssessmentCapability.py`
            - `__init__.py`
    - `reasoning_engines`
        - `__init__.py`
        - `GPTModels.py`
    - `layers`
        - `__init__.py`
        - `AspirationalLayer.py`
        - `GlobalStrategyLayer.py`
        - `AgentModelLayer.py`
        - `ExecutiveFunctionLayer.py`
        - `CognitiveControlLayer.py`
        - `TaskProsecutionLayer.py`
        - `test_layers.py`
        - `CognitiveLayer.py`


### Structure Description ###

This project is organized into several key modules, each containing various classes and scripts related to different aspects of the ACE model. 


#### layers ####

This directory contains classes related to the layers of the ACE model, including `AspirationalLayer`, `GlobalStrategyLayer`, `AgentModelLayer`, `ExecutiveFunctionLayer`, `CognitiveControlLayer`, `TaskProsecutionLayer`, and a test script.

#### orchestration ####

This directory contains classes related to the orchestration of the ACE model, including `CognitiveArchitecture.py`, `LayerHierarchy.py`, and a test script.

#### resource_manager ####

This directory contains classes related to managing resources. It includes `ResourceManager.py`, `Resource.py`, and subdirectories for dynamically created resources and predefined resources such as `CurrencyResource`, `SemanticMemoryResource`, `UserInteractionPlanResource`, and `WorldStateRssFeedsResource`.

#### capability_manager ####

This directory contains classes related to managing capabilities. It includes `Capability.py`, `CapabilityManager.py`, and subdirectories for dynamically created capabilities and predefined capabilities such as `MermaidGanttChartCapability`, `GenerateUserInteractionPlanCapability`, `EthicalDecisionMakingCapability`, and others.

#### product_manager ####

This directory contains classes related to managing products. It includes `ProductManager.py`, `Product.py`, and subdirectories for dynamically created products and predefined products such as `StakeholderAnalysisProduct`, `BudgetProposalProduct`, `ResourcePlanProduct`, and others.

#### reasoning_engines ####

This directory contains logic and interfaces for reasoning engines, including `GPTModels.py`.

## Environment Variables ##

The application expects several API keys to be available through environment
variables:

- `SERP_API_KEY`
- `BROWSERLESS_API_KEY`
- `OPENROUTER_API_KEY`

Copy `example.env` and populate these values, then place the resulting file in a
`vars/` directory at the project root. Keep the `vars/` directory unversioned so
your credentials remain private.
