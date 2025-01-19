from typing import Union

class TelemetryData:
    def __init__(self,
                 IsRaceOn: int,
                 TimestampMS: int,
                 EngineMaxRpm: float,
                 EngineIdleRpm: float,
                 CurrentEngineRpm: float,
                 AccelerationX: float,
                 AccelerationY: float,
                 AccelerationZ: float,
                 VelocityX: float,
                 VelocityY: float,
                 VelocityZ: float,
                 AngularVelocityX: float,
                 AngularVelocityY: float,
                 AngularVelocityZ: float,
                 Yaw: float,
                 Pitch: float,
                 Roll: float,
                 NormalizedSuspensionTravelFrontLeft: float,
                 NormalizedSuspensionTravelFrontRight: float,
                 NormalizedSuspensionTravelRearLeft: float,
                 NormalizedSuspensionTravelRearRight: float,
                 TireSlipRatioFrontLeft: float,
                 TireSlipRatioFrontRight: float,
                 TireSlipRatioRearLeft: float,
                 TireSlipRatioRearRight: float,
                 WheelRotationSpeedFrontLeft: float,
                 WheelRotationSpeedFrontRight: float,
                 WheelRotationSpeedRearLeft: float,
                 WheelRotationSpeedRearRight: float,
                 WheelOnRumbleStripFrontLeft: int,
                 WheelOnRumbleStripFrontRight: int,
                 WheelOnRumbleStripRearLeft: int,
                 WheelOnRumbleStripRearRight: int,
                 PositionX: float,
                 PositionY: float,
                 PositionZ: float,
                 Speed: float,
                 Gear: int,
                 RacePosition: int):
        self.IsRaceOn = IsRaceOn
        self.TimestampMS = TimestampMS
        self.EngineMaxRpm = EngineMaxRpm
        self.EngineIdleRpm = EngineIdleRpm
        self.CurrentEngineRpm = CurrentEngineRpm
        self.AccelerationX = AccelerationX
        self.AccelerationY = AccelerationY
        self.AccelerationZ = AccelerationZ
        self.VelocityX = VelocityX
        self.VelocityY = VelocityY
        self.VelocityZ = VelocityZ
        self.AngularVelocityX = AngularVelocityX
        self.AngularVelocityY = AngularVelocityY
        self.AngularVelocityZ = AngularVelocityZ
        self.Yaw = Yaw
        self.Pitch = Pitch
        self.Roll = Roll
        self.NormalizedSuspensionTravelFrontLeft = NormalizedSuspensionTravelFrontLeft
        self.NormalizedSuspensionTravelFrontRight = NormalizedSuspensionTravelFrontRight
        self.NormalizedSuspensionTravelRearLeft = NormalizedSuspensionTravelRearLeft
        self.NormalizedSuspensionTravelRearRight = NormalizedSuspensionTravelRearRight
        self.TireSlipRatioFrontLeft = TireSlipRatioFrontLeft
        self.TireSlipRatioFrontRight = TireSlipRatioFrontRight
        self.TireSlipRatioRearLeft = TireSlipRatioRearLeft
        self.TireSlipRatioRearRight = TireSlipRatioRearRight
        self.WheelRotationSpeedFrontLeft = WheelRotationSpeedFrontLeft
        self.WheelRotationSpeedFrontRight = WheelRotationSpeedFrontRight
        self.WheelRotationSpeedRearLeft = WheelRotationSpeedRearLeft
        self.WheelRotationSpeedRearRight = WheelRotationSpeedRearRight
        self.WheelOnRumbleStripFrontLeft = WheelOnRumbleStripFrontLeft
        self.WheelOnRumbleStripFrontRight = WheelOnRumbleStripFrontRight
        self.WheelOnRumbleStripRearLeft = WheelOnRumbleStripRearLeft
        self.WheelOnRumbleStripRearRight = WheelOnRumbleStripRearRight
        self.PositionX = PositionX
        self.PositionY = PositionY
        self.PositionZ = PositionZ
        self.Speed = Speed
        self.Gear = Gear
        self.RacePosition = RacePosition

    def __repr__(self):
        return f"TelemetryData({self.__dict__})"
