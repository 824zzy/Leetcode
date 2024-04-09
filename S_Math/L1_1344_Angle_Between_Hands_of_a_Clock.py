class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_angle = hour % 12 * 5 * 6 + minutes / 60 * 30
        m_angle = minutes * 6
        delta = abs(h_angle - m_angle)
        return min(delta, 360 - delta)
