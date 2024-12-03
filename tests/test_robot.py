import unittest
from typing import Self

from dtalk_robot import Robot


class TestRobot(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self: Self) -> None:
        self.robot: Robot = Robot(access_token="access_token", secret="secret")

    async def test_robot(self: Self) -> None:
        pass

    async def asyncTearDown(self: Self) -> None:
        await self.robot.close()


if __name__ == "__main__":
    unittest.main()
