from threading import Thread
from unittest import TestCase

from ioc import IoC
from scope_base import InitScopesCommand, Scope


class ExceptionThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ex = None

    def run(self):
        try:
            super().run()
        except BaseException as e:
            self.ex = e

    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        if self.ex is not None:
            raise self.ex


class TestScopeBasedIoC(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        InitScopesCommand().execute()

    def test_root_scope_is_available(self):
        self.assertIsInstance(IoC.resolve('Scopes.Root'), Scope)

    def test_default_current_scope_is_root(self):
        root_scope = IoC.resolve('Scopes.Root')
        current_scope = IoC.resolve('Scopes.Current')
        self.assertEqual(root_scope, current_scope)

    def test_multithreading(self):
        scope = IoC.resolve('Scopes.New', IoC.resolve('Scopes.Root'))
        IoC.resolve('Scopes.Current.Set', scope).execute()
        IoC.resolve('IoC.Register', 'dependency', lambda: 1).execute()

        def thread_logic(parent_scope, thread_number):
            thread_scope = IoC.resolve('Scopes.New', parent_scope)
            IoC.resolve('Scopes.Current.Set', thread_scope).execute()
            self.assertEqual(1, IoC.resolve('dependency'))
            IoC.resolve('IoC.Register', 'thread_dependency', lambda: thread_number).execute()
            self.assertEqual(thread_number, IoC.resolve('thread_dependency'))

        threads = list()
        for i in range(100):
            thread = ExceptionThread(target=thread_logic, args=(scope, i))
            threads.append(thread)

        # start threads
        for thread in threads:
            thread.start()

        # wait for threads to finish
        for thread in threads:
            thread.join()

        with self.assertRaisesRegex(Exception, "Unknown dependency 'thread_dependency'"):
            IoC.resolve('thread_dependency')
