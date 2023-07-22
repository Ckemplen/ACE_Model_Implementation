from orchestration import CognitiveArchitecture

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    project_management_agent = CognitiveArchitecture()

    # Amend the state of the aspirational layer with new mission/values
    # Demo mission and values drawn from Association of Project Managers (APM) mission and values statements
    config_data = {
        'mission': 'Advance the science, theory and practice of project and programme management for the public benefit',
        'values': ['honesty', 'integrity', 'impartiality', 'objectivity', 'progressive', 'thoughtful', 'warm',
                   'excellent']}

    project_management_agent.aspirational_layer.amend_state(config_data)

    """DEVELOPMENT GOAL MISSION: Comprehensive Project Initiation 
    
    As a chartered member of the Association for Project Management (APM), I would expect the successful completion 
    of the project initiation phase to result in a comprehensive suite of product_manager and documentation. These 
    deliverables are essential to establish a solid foundation for the project and ensure that all stakeholders have 
    a clear understanding of its objectives, scope, constraints, and risks. The following are the typical product_manager 
    and documentation that should be completed during the project initiation phase:

    Project Charter: The project charter serves as the formal document that authorizes the project and outlines its 
    objectives, scope, deliverables, stakeholders, and high-level timelines. It is usually created by the project 
    sponsor or initiator.
    
    Business Case: The business case justifies the need for the project and outlines its expected benefits, costs, 
    and risks. It helps stakeholders understand the rationale behind the project and evaluate its viability.
    
    Stakeholder Analysis: This document identifies all key stakeholders, their roles, interests, and potential influence 
    on the project. Understanding stakeholders is crucial for effective communication and managing expectations.
    
    Project Scope Statement: The scope statement defines the boundaries of the project, including what is included and 
    excluded. It clarifies the project's objectives and deliverables and helps manage scope creep.
    
    Risk Management Plan: The risk management plan identifies potential risks, assesses their impact and probability, 
    and outlines strategies to mitigate or respond to them effectively.
    
    Project Organization Chart: The organization chart defines the project team structure, roles, and reporting 
    lines. It helps clarify responsibilities and ensures everyone knows their place in the project hierarchy.
    
    Project Schedule: A high-level project schedule outlines the major project milestones and estimated timelines. It 
    provides an overview of the project's timeline and helps identify critical paths.
    
    Resource Plan: The resource plan identifies the types and quantities of resources required for the project, 
    including personnel, equipment, and materials.
    
    Communication Plan: The communication plan defines how project information will be distributed, who will be 
    responsible for communication, and the frequency and format of communication.
    
    Quality Management Plan: The quality management plan outlines the quality standards, processes, and methodologies to 
    be used during the project to ensure that deliverables meet the required level of quality.
    
    Procurement Strategy: If the project involves external procurement, a procurement strategy will outline the approach 
    to sourcing goods or services and the criteria for selecting vendors.
    
    Project Approval Documentation: Any approvals or sign-offs required to proceed with the project should be 
    documented, including approval from senior management or the project governance board.
    
    Lessons Learned from Pre-Project Phase: If applicable, any lessons learned from the pre-project phase (feasibility 
    study, concept development, etc.) should be documented to inform the project initiation phase.
    
    Legal and Regulatory Review: Documentation related to legal and regulatory compliance requirements that impact the 
    project should be gathered and understood.
    
    Budget Proposal: The budget proposal outlines the estimated project costs, including expenses and resource 
    requirements, to secure funding approval.
    
    By completing this suite of product_manager and documentation, the project team can ensure a clear understanding of the 
    project's objectives, scope, risks, and responsibilities. This sets the stage for a successful project execution 
    phase and facilitates effective communication and decision-making throughout the project's lifecycle.
    """
