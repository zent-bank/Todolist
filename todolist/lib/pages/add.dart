import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

import 'package:todolist/utils/constants.dart';

class AddPage extends StatefulWidget {
  const AddPage({ Key? key }) : super(key: key);

  @override
  _AddPageState createState() => _AddPageState();
}

class _AddPageState extends State<AddPage> {
  TextEditingController titleController = new TextEditingController();
  TextEditingController detailController = new TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('เพิ่มรายการใหม่'),
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
                  await postTodo();
                  setState(() {
                    titleController.clear();
                    detailController.clear();
                  });
                }, 
                child: Text("เพิ่มรายการ"),
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

  Future postTodo() async {
    var url = Uri.http(API_ENDPOINT, '/api/post-todolist');
    Map<String, String> header = {"Content-Type":"application/json"};
    String jsondata = '{"title":"${titleController.text}","detail": "${detailController.text}"}';
    print(jsondata);
    var response = await http.post(url,headers: header, body: jsondata);
    print('response: ${response.body}');
  }
}