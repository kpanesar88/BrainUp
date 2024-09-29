from typing import Tuple, Callable, TypeVar

from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection
from multiprocessing import freeze_support

T = TypeVar('T') 

def model_loop(model_loader: Callable[[], Callable[[str], T]]) -> Callable[[], Tuple[Connection, Connection, Process]]:
    freeze_support()
    def tmp() -> Tuple[Connection, Connection, Process]:
        freeze_support()
        input_recv, input_sender = Pipe(duplex=False)
        output_recv, output_sender = Pipe(duplex=False)

        process = Process(
            target=_loop,
            args=[model_loader, input_recv, output_sender]
        )

        process.start()

        return (input_sender, output_recv, process)
    return tmp

def _loop(model_loader: Callable[[], Callable[[str], T]], input_recv: Connection, output_sender: Connection):
    model = model_loader()

    while True:
        path = input_recv.recv()
        output_sender.send((
            path,
            model(
                path
            )
        ))