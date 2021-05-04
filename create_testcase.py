import random
def assign(file_output):
    x=random.randint(0,50)
    y=random.randint(0,50)
    n=random.randint(30,100)
    m=random.randint(10,int(n/2))
    with open(file_output, 'w') as out_file:
        out_file.write('%s ' %x)
        out_file.write('%s\n' %y)
        out_file.write('%s ' %n)
        out_file.write('%s\n' %m)
        for i in range(n):
            out_file.write('%s ' %random.randint(1,50))
            out_file.write('%s ' %random.randint(1,50))
            out_file.write('%s ' %random.randint(1,100))
            out_file.write('%s' %random.randint(1,100))
            out_file.write('\n')
assign('input.txt')