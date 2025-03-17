from pila import Stack

if __name__ == '__main__':
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')
    stack.push('e')
    stack.print_stack()
    stack.draw_stack('pila_inicial')
    print('---------------------------')

    value = stack.pop()
    print('Valor eliminado: ', value)
    stack.print_stack()
    stack.draw_stack('pila_final')
