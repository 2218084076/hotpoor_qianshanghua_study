import tornado.ioloop
import tornado.web
import sys
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello,Teryy")
class ReadDemoHandler(tornado.web.RequestHandler):
    def get(self):
        f=open("demo.txt","r")
        self.write(f.read())

def make_app():
    return tornado.web.Application([
        (r"/demo",ReadDemoHandler),
        (r"/",MainHandler)
    ])
if __name__ == "__main__":
    a=sys.argv
    print(a)
    b=a[1:]
    print(b)
    c={}
    for i in range(0,len(b),2):
        c[b[i]]=b[i+1]
    port=int(c.get("--port","8888"))
    app=make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()