#_*_coding:utf-8_*_
import asyncio

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()  #await是异步等待, 既然你已经知道了控制权会被交出去, 那么就说明他自己是不可能自己恢复的, 必须等待外部程序(python解释器)利用send重新启动切换时的执行现场.
    while True:
        line = await reader.readline()
        if line == b'\r\n': #readline函数如果返回了\r\n就说明这一行是空行; //而http协议就是根据空行进行分割的, 注意区分空行和行尾有换行符
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''问题1：遇到await处，把控制权交给指定的协程，但如何知道这个协程什么时候能执行完成并返还控制权呢？

首先, await是异步等待, 既然你已经知道了控制权会被交出去, 那么就说明他自己是不可能自己恢复的, 必须等待外部程序(python解释器)利用send重新启动切换时的执行现场.

#调度器应该会有类似下面的代码, 恢复执行现场.

#以监听stdin的输入事件为例
selector = selectors.DefaultSelector()
selector.register(sys.stdin, selectors.EVENT_READ)

#系统使用select等方式监听事件
for key, mask in self._selector.select(0):
    for task in self._tasks_waiting_on_stdin:
        # stdin可用, 将其send给协程中断的上下文.
        task.send(sys.stdin)

问题2：drain这个协程作用貌似刷新写入的缓冲区，那这个wirte具体把‘请求头数据’写入到了哪里呢？

不甚了解asyncio模块的writer函数, 但是从代码来看, 它是直接写出到TCP连接的, 也就是http的sever端.

问题3：b'\r\n'处，为什么能够判断分离header和body数据，返回header的每一行都有换行啊，这样难道不会在打印第一条header信息后就会被break了？

这里你可能有两个问题, 一个是不是特别清楚HTTP协议, 或者你不是特别清楚python的readline函数; readline函数如果返回了\r\n就说明这一行是空行;
而http协议就是根据空行进行分割的, 注意区分空行和行尾有换行符