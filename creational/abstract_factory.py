"""
    In Java and other languages, the Abstract Factory Pattern serves to provide an interface for
    creating related/dependent objects without need to specify their actual class.
    The idea is to abstract the creation of objects depending on business logic, platform choice, etc.

    In Python, the interface we use is simply a callable, which is "builtin" interface in Python, and in
    normal circumstances we can simply use the class itself as that callable, because classes are first class
    objects in Python.

    Below example:
    Uses abstract factory pattern to select DB TNS_ALIAS depending on environment set (DEV, SIT, PROD)

"""


import os
from os.path import join, dirname
from dotenv import load_dotenv
from typing import Type


class Database:

    def __init__(self, env: str) -> None:
        self.name = env

    def create_tns(self):
        print("Connecting to dummy")


#  If no __init__() method is implemented in the inherited class, then the parent __init__()
#  will be called automatically when an object of the inherited class is created.

class DEV(Database):

    def create_tns(self):
        print("Connecting to DEV at ", "NABTDL01_SVC")


class SIT(Database):

    def create_tns(self):
        print("Connecting to SIT at ", "NABTST01_SVC")


class QA(Database):

    def create_tns(self):
        print("Connecting to QA at ", "QABTSA01_SVC")


class PROD(Database):

    def create_tns(self):
        print("Connecting to PROD at ", "PALBTS01_PRIM")


class DatabaseFactory:

    def __init__(self, env: Type[Database]):
        self.env = env

    def create(self):
        return self.env("abc")


print("Testing Abstract Factory")

load_dotenv(join(dirname(__file__), ".env"))
env_var = os.environ.get("ENV")

DatabaseFactory(eval("DEV")).create().create_tns()

DatabaseFactory(eval(env_var)).create().create_tns()

DatabaseFactory(PROD).create().create_tns()
