from orchestration import CognitiveArchitecture


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cognition_machine = CognitiveArchitecture()

    # Amend the state of the aspirational layer with new mission/values
    config_data = {
        'mission': 'Make access to lifelong flexible loan funded study a reality within the UK',
        'values': ['honesty', 'integrity', 'impartiality', 'objectivity']
    }
    cognition_machine.aspirational_layer.amend_state(config_data)


