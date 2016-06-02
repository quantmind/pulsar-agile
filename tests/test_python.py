import tests

import agile


def test_function(cmd):
    return 'OK'


class TestPython(tests.AgileTest):
    config_file = 'tests/configs/python.json'

    async def test_task(self):
        app = await self.app(tasks=["test"])
        self.assertEqual(app.cfg.tasks, ["test"])
        await self.wait.assertEqual(app(), 0)
        self.assertEqual(app.context['test1'], 'OK')

    async def test_task2(self):
        app = await self.app(tasks=["version"])
        await self.wait.assertEqual(app(), 0)
        self.assertEqual(app.context['agile_version'], agile.__version__)
