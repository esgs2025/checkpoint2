// Auto-generated. Do not edit!

// (in-package mir_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let BrakeState = require('./BrakeState.js');
let GripperState = require('./GripperState.js');
let HeightState = require('./HeightState.js');

//-----------------------------------------------------------

class HookExtendedStatus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.available = null;
      this.brake = null;
      this.gripper = null;
      this.height = null;
      this.angle = null;
      this.qr_marker_name = null;
    }
    else {
      if (initObj.hasOwnProperty('available')) {
        this.available = initObj.available
      }
      else {
        this.available = false;
      }
      if (initObj.hasOwnProperty('brake')) {
        this.brake = initObj.brake
      }
      else {
        this.brake = new BrakeState();
      }
      if (initObj.hasOwnProperty('gripper')) {
        this.gripper = initObj.gripper
      }
      else {
        this.gripper = new GripperState();
      }
      if (initObj.hasOwnProperty('height')) {
        this.height = initObj.height
      }
      else {
        this.height = new HeightState();
      }
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = 0.0;
      }
      if (initObj.hasOwnProperty('qr_marker_name')) {
        this.qr_marker_name = initObj.qr_marker_name
      }
      else {
        this.qr_marker_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HookExtendedStatus
    // Serialize message field [available]
    bufferOffset = _serializer.bool(obj.available, buffer, bufferOffset);
    // Serialize message field [brake]
    bufferOffset = BrakeState.serialize(obj.brake, buffer, bufferOffset);
    // Serialize message field [gripper]
    bufferOffset = GripperState.serialize(obj.gripper, buffer, bufferOffset);
    // Serialize message field [height]
    bufferOffset = HeightState.serialize(obj.height, buffer, bufferOffset);
    // Serialize message field [angle]
    bufferOffset = _serializer.float32(obj.angle, buffer, bufferOffset);
    // Serialize message field [qr_marker_name]
    bufferOffset = _serializer.string(obj.qr_marker_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HookExtendedStatus
    let len;
    let data = new HookExtendedStatus(null);
    // Deserialize message field [available]
    data.available = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [brake]
    data.brake = BrakeState.deserialize(buffer, bufferOffset);
    // Deserialize message field [gripper]
    data.gripper = GripperState.deserialize(buffer, bufferOffset);
    // Deserialize message field [height]
    data.height = HeightState.deserialize(buffer, bufferOffset);
    // Deserialize message field [angle]
    data.angle = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [qr_marker_name]
    data.qr_marker_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.qr_marker_name);
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mir_msgs/HookExtendedStatus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7a4c65a73248ad57ddff2231bb564f0d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool available
    
    BrakeState brake
    
    GripperState gripper
    
    HeightState height
    
    float32 angle
    
    string qr_marker_name
    
    ================================================================================
    MSG: mir_msgs/BrakeState
    uint8 UNKNOWN = 0
    uint8 INITIALIZING = 1
    uint8 HOMING = 2
    uint8 ACTIVE = 3
    uint8 INACTIVE = 4
    uint8 ACTIVATING = 5
    uint8 DEACTIVATING = 6
    uint8 ERROR = 7
    
    uint8 state
    
    ================================================================================
    MSG: mir_msgs/GripperState
    uint8 LOCK_UNKNOWN = 0
    uint8 LOCK_HOMING = 1
    uint8 LOCK_OPEN = 2
    uint8 LOCK_OPENING = 3
    uint8 LOCK_CLOSED = 4
    uint8 LOCK_CLOSING = 6
    uint8 LOCK_ERROR = 9
    
    uint8 state
    
    ================================================================================
    MSG: mir_msgs/HeightState
    uint8 HEIGHT_UNKNOWN = 0
    uint8 HEIGHT_HOMING = 1
    uint8 HEIGHT_IDLE = 2
    uint8 HEIGHT_CHANGING = 3
    uint8 HEIGHT_ERROR = 4
    
    uint8 state
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new HookExtendedStatus(null);
    if (msg.available !== undefined) {
      resolved.available = msg.available;
    }
    else {
      resolved.available = false
    }

    if (msg.brake !== undefined) {
      resolved.brake = BrakeState.Resolve(msg.brake)
    }
    else {
      resolved.brake = new BrakeState()
    }

    if (msg.gripper !== undefined) {
      resolved.gripper = GripperState.Resolve(msg.gripper)
    }
    else {
      resolved.gripper = new GripperState()
    }

    if (msg.height !== undefined) {
      resolved.height = HeightState.Resolve(msg.height)
    }
    else {
      resolved.height = new HeightState()
    }

    if (msg.angle !== undefined) {
      resolved.angle = msg.angle;
    }
    else {
      resolved.angle = 0.0
    }

    if (msg.qr_marker_name !== undefined) {
      resolved.qr_marker_name = msg.qr_marker_name;
    }
    else {
      resolved.qr_marker_name = ''
    }

    return resolved;
    }
};

module.exports = HookExtendedStatus;
