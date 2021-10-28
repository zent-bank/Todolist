import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

import 'package:todolist/pages/add.dart';
import 'package:todolist/pages/udpate_todolist.dart';


class Todolist extends StatefulWidget {
  const Todolist({ Key? key }) : super(key: key);

  @override
  _TodolistState createState() => _TodolistState();
}

class _TodolistState extends State<Todolist> {
  List toDoListItems = [];

  @override
  void initState() {
    super.initState();
    getTodolist();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(context, 
            MaterialPageRoute(builder: (context) => AddPage())
          ).then((value) {
            getTodolist();
          });
        },
        child: Icon(Icons.add),
      ),
      appBar: AppBar(
        title: Text('All TodoList'),
        actions: [
          IconButton(
            onPressed: () {
              getTodolist();
            }, 
            icon: Icon(Icons.refresh,color: Colors.white,),
          )
        ],
      ),
      body: todolistCreate()
    );
  }

  Widget todolistCreate() {
    return ListView.builder(
      itemCount: toDoListItems.length,
      itemBuilder: (context, index){
        return Card(
          child: ListTile(
            title: Text("${toDoListItems[index]['title']}"),
            onTap: () {
              Navigator.push(
                context, 
                MaterialPageRoute(builder: (context) => 
                  UpdatePage(
                    toDoListItems[index]['id'], 
                    toDoListItems[index]['title'], 
                    toDoListItems[index]['detail']
                  )
                )
              ).then((value) {
                print(value);
                if(value == 'deleted'){
                  final snackBar = SnackBar(content: const Text('ลบรายการเรียบร้อยแล้ว'));
                  ScaffoldMessenger.of(context).showSnackBar(snackBar);
                }
                getTodolist();
              });
            },
          ),
        );
      }
    );
  }

  Future<void> getTodolist() async {
    var url = Uri.http('192.168.1.121:8000','/api/all-todolist');
    var response = await http.get(url);
    // var result = json.decode(response.body);
    var result = jsonDecode(utf8.decode(response.bodyBytes));
    print(result);
    setState(() {
      toDoListItems = result;
    });
  }
}