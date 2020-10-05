#!/usr/bin/env python
"""A Pure Python Raytracer"""
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material
import argparse
import importlib
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('scene', help='Path to scene')
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)
    
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))

    # WIDTH = 320
    # HEIGHT = 200
    # camera = Vector(0, 0, -1)
    # objects = [Sphere(Point(0, 0, 0), 0.5, Material(Color.from_hex('#FF0000')))]
    # lights = [Light(Point(1.5, -0.5, -10.0), Color.from_hex('#FFFFFF'))]
    # scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    # engine = RenderEngine()
    # image = engine.render(scene)

    # Was open(args.imageout, 'w')
    with open(mod.RENDERED_IMG, 'w') as img_file:
        image.write_ppm(img_file)


if __name__ == '__main__':
    main()

