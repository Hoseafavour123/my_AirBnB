#!/usr/bin/python3
import cmd
import os
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""This module defines the entry of the commandline interpreter"""


classes = {

        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }



class HBNBCommand(cmd.Cmd):
    """Commandline interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        print()
        return True

    def emptyline(self):
        """overwrites the method in cmd"""
        return

    def do_create(self, line):
        """Create a new instance of BaseModel"""

        class_name, args, line = self.parseline(line)
        if class_name is None:
            print("** class name missing **")
        elif class_name not in classes:
            print("** class name doesn't exist **")
        else:
            model = classes[class_name]()
            model.save()
            print(f"{model.id}")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
            name and id."""
        class_name, obj_id, line = self.parseline(line)
        if class_name is None:
            print("** class name missing **")
        elif class_name not in classes:
            print("** class doesn't exist **")
        elif obj_id is None or obj_id == "":
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            inst_key = None
            for key, val in obj_dict.items():
                if key == f"{class_name}.{obj_id}":
                    inst_key = key
            if inst_key is not None:
                print(f"[{class_name}] ({obj_id}) {obj_dict[key]}")
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an instance based on the class name and id."""
        class_name, obj_id, line = self.parseline(line)
        if class_name is None:
            print("** class name is missinng **")
        elif class_name not in classes:
            print("** class doesn't exist **")
        elif obj_id is None or obj_id == "":
            print("** instance id missing **")
        else:
            all_inst = storage.all()
            key = None
            for k, v in all_inst.items():
                if k == f"{class_name}.{obj_id}":
                    key = k
            if key is not None:
                del all_inst[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints the string representation of all instances based or not on
            the class name."""
        class_name, args, line = self.parseline(line)

        inst_store = storage.all()
        inst_list = []
        if class_name is None or class_name == "":
            for k, v in inst_store.items():
                obj_id = v["id"]
                obj_dict = v

                inst_str = f"[{v['__class__']}] ({obj_id}) {obj_dict}"
                inst_list.append(inst_str)
            print(inst_list)

        elif class_name in classes:
            for k, v in inst_store.items():
                if v["__class__"] == class_name:
                    obj_id = v["id"]
                    obj_dict = v

                    inst_str = f"[{class_name}] ({obj_id}) {obj_dict}"
                    inst_list.append(inst_str)
            print(inst_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        class_name, args, line = self.parseline(line)
        if class_name is None or class_name == "":
            print("** class name missing **")
        elif class_name not in classes:
            print("** class name doesn't exist **")
        elif args is None or args == "":
            print("** instance id missing **")
        elif len(args.split()) < 2:
            print("** attribute name missing **")
        elif len(args.split()) < 3:
            print("** value missing **")
        else:
            Id, attr, val = args.split()[:3]
            all_inst = storage.all()
            inst_key = None
            for k, v in all_inst.items():
                if v["__class__"] == class_name and v["id"] == Id:
                    inst_key = k
                    inst_dict = v
            if inst_key == None:
                print("** no instance found **")
            else:
                inst_model = classes[class_name](**inst_dict)
                if hasattr(inst_model, attr):
                    attr_type = type(getattr(inst_model, attr))
                    setattr(inst_model, attr, attr_type(val.strip('"')))
                else:
                    setattr(inst_model, attr, val.strip('"'))

                all_inst[inst_key] = inst_model.to_dict()
                storage.save()

    def default(self, line):
        """The default method."""
        class_name, action, line = self.parseline(line)
        inst_dict = storage.all()
        count = 0

        if action == ".all()":
            self.do_all(class_name)

        elif action == ".count()":
            for k, v in inst_dict.items():
                if v["__class__"] == class_name:
                    count += 1
            print(count)
 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
