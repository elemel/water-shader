import pyglet
from pyglet.gl import *
import shader

class MyShader(shader.Shader):
    def __enter__(self):
        self.bind()
        return self

    def __exit__(self, *args):
        self.unbind()

class MyWindow(pyglet.window.Window):
    def __init__(self, **kwargs):
        super(MyWindow, self).__init__(**kwargs)
        frag = pyglet.resource.file('water.frag').read()
        self.shader = MyShader(frag=[frag])
        self.time = 0.0

    def on_draw(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(0.2, 0.8, 1.0, 1.0)
        self.clear()
        with self.shader:
            self.shader.uniformf('time', self.time)
            self.shader.uniformf('surface_y', float(self.height // 2))
            self.shader.uniformf('wave_height', 15.0)
            self.shader.uniformf('wave_length', 100.0)
            self.shader.uniformf('wave_speed', 0.15)
            glBegin(GL_QUADS)
            glColor4f(0.0, 0.2, 0.3, 1.0)
            glTexCoord2i(0, 0)
            glVertex2i(0, 0)
            glTexCoord2i(self.width, 0)
            glVertex2i(self.width, 0)
            glColor4f(0.0, 0.8, 1.0, 1.0)
            glTexCoord2i(self.width, self.height)
            glVertex2i(self.width, self.height)
            glTexCoord2i(0, self.height)
            glVertex2i(0, self.height)
            glEnd()

    def step(self, dt):
        self.time += dt

def main():
    config = pyglet.gl.Config(double_buffer=True, sample_buffers=1, samples=4,
                              depth_size=8)
    window = MyWindow(fullscreen=True, config=config)
    pyglet.clock.schedule_interval(window.step, 1.0 / 60.0)
    pyglet.app.run()

if __name__ == '__main__':
    main()
