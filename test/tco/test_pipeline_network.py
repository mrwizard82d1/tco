import unittest

import tco


class TestPipelineNetwork(unittest.TestCase):
    def test_is_connected(self):
        sut = tco.PipelineNetwork()

        self.add_no_cost_segments(sut)

        self.assertTrue(sut.is_connected('Midland', 'Evansville'))

    def test_is_not_connected(self):
        sut = tco.PipelineNetwork()

        self.add_no_cost_segments(sut)

        self.assertFalse(sut.is_connected('Vancouver', 'Evansville'))

    @staticmethod
    def add_no_cost_segments(sut):
        sut.add_segment('Houston', 'Midland')
        sut.add_segment('Houston', 'OK City')
        sut.add_segment('Houston', 'St. Louis')
        sut.add_segment('Houston', 'New Orleans')

        sut.add_segment('Midland', 'OK City')
        sut.add_segment('Midland', 'Houston')

        sut.add_segment('OK City', 'St. Louis')
        sut.add_segment('OK City', 'New Orleans')
        sut.add_segment('OK City', 'Houston')
        sut.add_segment('OK City', 'Midland')

        sut.add_segment('St. Louis', 'Evansville')
        sut.add_segment('St. Louis', 'New Orleans')
        sut.add_segment('St. Louis', 'Houston')
        sut.add_segment('St. Louis', 'OK City')

        sut.add_segment('Evansville', 'New Orleans')
        sut.add_segment('Evansville', 'St. Louis')

        sut.add_segment('New Orleans', 'Houston')
        sut.add_segment('New Orleans', 'OK City')
        sut.add_segment('New Orleans', 'St. Louis')
        sut.add_segment('New Orleans', 'Evansville')

        sut.add_segment('Vancouver', 'Chicago')
        sut.add_segment('Vancouver', 'North Platte')

        sut.add_segment('Chicago', 'Toledo')
        sut.add_segment('Chicago', 'Columbus')
        sut.add_segment('Chicago', 'North Platte')
        sut.add_segment('Chicago', 'Vancouver')

        sut.add_segment('North Platte', 'Vancouver')
        sut.add_segment('North Platte', 'Chicage')

        sut.add_segment('Toledo', 'Columbus')
        sut.add_segment('Toledo', 'Chicago')

        sut.add_segment('Columbus', 'Chicago')
        sut.add_segment('Columbus', 'Toledo')

    @staticmethod
    def add_toll_segments(sut):
        sut.add_segment('Houston', 'Midland', 9)
        sut.add_segment('Houston', 'OK City', 7)
        sut.add_segment('Houston', 'St. Louis', 11)
        sut.add_segment('Houston', 'New Orleans', 4)

        sut.add_segment('Midland', 'OK City', 6)
        sut.add_segment('Midland', 'Houston', 9)

        sut.add_segment('OK City', 'St. Louis', 8)
        sut.add_segment('OK City', 'New Orleans', 8)
        sut.add_segment('OK City', 'Houston', 7)
        sut.add_segment('OK City', 'Midland', 6)
        sut.add_segment('OK City', 'North Platte', 16)

        sut.add_segment('St. Louis', 'Chicago', 4)
        sut.add_segment('St. Louis', 'Evansville', 1)
        sut.add_segment('St. Louis', 'New Orleans', 12)
        sut.add_segment('St. Louis', 'Houston', 11)
        sut.add_segment('St. Louis', 'OK City', 8)

        sut.add_segment('Evansville', 'New Orleans', 10)
        sut.add_segment('Evansville', 'St. Louis', 1)
        sut.add_segment('Evansville', 'Chicago', 5)
        sut.add_segment('Evansville', 'Columbus', 2)

        sut.add_segment('New Orleans', 'Houston', 4)
        sut.add_segment('New Orleans', 'OK City', 8)
        sut.add_segment('New Orleans', 'St. Louis', 12)
        sut.add_segment('New Orleans', 'Evansville', 10)

        sut.add_segment('Vancouver', 'Chicago', 21)
        sut.add_segment('Vancouver', 'North Platte', 12)

        sut.add_segment('Chicago', 'Toledo', 3)
        sut.add_segment('Chicago', 'Columbus', 4)
        sut.add_segment('Chicago', 'Evansville', 5)
        sut.add_segment('Chicago', 'St. Louis', 4)
        sut.add_segment('Chicago', 'North Platte', 5)
        sut.add_segment('Chicago', 'Vancouver', 21)

        sut.add_segment('North Platte', 'Vancouver', 12)
        sut.add_segment('North Platte', 'Chicago', 5)
        sut.add_segment('North Platte', 'OK City', 16)

        sut.add_segment('Toledo', 'Columbus', 1)
        sut.add_segment('Toledo', 'Chicago', 3)

        sut.add_segment('Columbus', 'Chicago', 4)
        sut.add_segment('Columbus', 'Toledo', 1)
        sut.add_segment('Columbus', 'Evansville', 2)

    def test_minimum_cost_route_from_houston(self):
        sut = tco.PipelineNetwork()

        self.add_toll_segments(sut)

        actual_route = sut.minimum_cost_route('Houston', 'Toledo')[0]

        self.assertEqual(actual_route, ['Houston', 'St. Louis', 'Evansville', 'Columbus', 'Toledo'])

    def test_minimum_cost_route_cost_from_houston(self):
        sut = tco.PipelineNetwork()

        self.add_toll_segments(sut)

        actual_cost = sut.minimum_cost_route('Houston', 'Toledo')[1]

        self.assertEqual(actual_cost, 15)

    def test_minimum_cost_route_from_midland(self):
        sut = tco.PipelineNetwork()

        self.add_toll_segments(sut)

        actual_route = sut.minimum_cost_route('Midland', 'Toledo')[0]

        self.assertEqual(actual_route, ['Midland', 'OK City', 'St. Louis', 'Evansville', 'Columbus', 'Toledo'])

    def test_minimum_cost_route_cost_from_midland(self):
        sut = tco.PipelineNetwork()

        self.add_toll_segments(sut)

        actual_cost = sut.minimum_cost_route('Midland', 'Toledo')[1]

        self.assertEqual(actual_cost, 16)


if __name__ == '__main__':
    unittest.main()
