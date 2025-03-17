from cola import Queue

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.enqueue('e')
    queue.print_queue()
    queue.draw_queue('cola_inicial')
    print('---------------------------')

    queue.dequeue()
    queue.print_queue()
    queue.draw_queue('cola_final')
