# test_layers.py

import pytest
from layers import AspirationalLayer, GlobalStrategyLayer, AgentModelLayer, ExecutiveFunctionLayer, CognitiveControlLayer, TaskProsecutionLayer

def test_AspirationalLayer_initialization():
    # Test that an AspirationalLayer instance can be created without errors
    layer = AspirationalLayer()
    assert layer is not None

def test_GlobalStrategyLayer_initialization():
    # Test that a GlobalStrategyLayer instance can be created without errors
    layer = GlobalStrategyLayer()
    assert layer is not None

def test_AgentModelLayer_initialization():
    # Test that an AgentModelLayer instance can be created without errors
    layer = AgentModelLayer()
    assert layer is not None

def test_ExecutiveFunctionLayer_initialization():
    # Test that an ExecutiveFunctionLayer instance can be created without errors
    layer = ExecutiveFunctionLayer()
    assert layer is not None

def test_CognitiveControlLayer_initialization():
    # Test that a CognitiveControlLayer instance can be created without errors
    layer = CognitiveControlLayer()
    assert layer is not None

def test_TaskProsecutionLayer_initialization():
    # Test that a TaskProsecutionLayer instance can be created without errors
    layer = TaskProsecutionLayer()
    assert layer is not None

def test_CognitiveLayer_methods():
    # Test the methods in the CognitiveLayer class
    layer = AspirationalLayer()  # or any other layer class

    # Test pass_up method
    data = "test_data"
    layer.pass_up(data)
    assert not layer.up_queue.empty()

    # Test pass_down method
    layer.pass_down(data)
    assert not layer.down_queue.empty()

    # Test receive_from_above method
    received_data = layer.receive_from_above()
    assert received_data == data

    # Test receive_from_below method
    received_data = layer.receive_from_below()
    assert received_data == data

    # Test amend_state method
    new_state = {"mission": "new_mission", "values": ["new_value1", "new_value2"]}
    layer.amend_state(new_state)
    assert layer.mission == "new_mission"
    assert layer.values == ["new_value1", "new_value2"]
