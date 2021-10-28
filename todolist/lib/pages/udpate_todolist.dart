import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';

class UpdatePage extends StatefulWidget {
  final id;
  final title;
  final detail;
  const UpdatePage(this.id, this.title, this.detail);

  @override
  _UpdatePageState createState() => _UpdatePageState();
}

class _UpdatePageState extends State<UpdatePage> {

  TextEditingController titleController = new TextEditingController();
  TextEditingController detailController = new TextEditingController();
  int _id = 0;
  String _title = "";
  String _detail = "";

  @override
  void initState() {
    super.initState();
    _id = widget.id;
    _title = widget.title;
    _detail = widget.detail;
    titleController.text = _title;
    detailController.text = _detail;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('แก้ไข'),
        actions: [
          IconButton(
            onPressed: () {
              print("Delete ID: $_id");
              deleteTodo();
              Navigator.pop(context,'deleted');
            }, 
            icon: Icon(Icons.delete,color: Colors.red,),
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: ListView(
          children: [
            TextField(
              controller: titleController,
              decoration: InputDecoration(
                labelText: "รายการที่ต้องทำ", 
                border: OutlineInputBorder()),
            ),
            SizedBox(height: 30,),
            TextField(
              keyboardType: TextInputType.multiline,
              minLines: 4,
              maxLines: 8,
              controller: detailController,
              decoration: InputDecoration(
                labelText: "รายละเอียด", 
                border: OutlineInputBorder()),
            ),
            SizedBox(height: 30,),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 50),
              child: ElevatedButton(
                onPressed: () async {
                  print('-------------');
                  print('title: ${titleController.text}');
                  print('detail: ${detailController.text}');
                  await updateTodo();
                  final snackBar = SnackBar(content: const Text('บันทึกรายการเรียบร้อยแล้ว'));
                  ScaffoldMessenger.of(context).showSnackBar(snackBar);
                }, 
                child: Text("แก้ไขรายการ"),
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(Colors.blue),
                  padding: MaterialStateProperty.all(EdgeInsets.fromLTRB(50, 20, 50, 20)),
                  textStyle: MaterialStateProperty.all(TextStyle(fontSize: 20))
                ),
              ),
            ),

          ],
        ),
      ),
    );
  }

  Future updateTodo() async {
    var url = Uri.http('192.168.1.121:8000', '/api/update-todolist/$_id');
    Map<String, String> header = {"Content-Type":"application/json"};
    String jsondata = '{"title":"${titleController.text}","detail": "${detailController.text}"}';
    print(jsondata);
    var response = await http.put(url,headers: header, body: jsondata);
    print('response: ${response.body}');
  }

  Future deleteTodo() async {
    var url = Uri.http('192.168.1.121:8000', '/api/delete-todolist/$_id');
    Map<String, String> header = {"Content-Type":"application/json"};
    String jsondata = '{"title":"${titleController.text}","detail": "${detailController.text}"}';
    print(jsondata);
    var response = await http.delete(url,headers: header, body: jsondata);
    print('response: ${response.body}');
  }
}