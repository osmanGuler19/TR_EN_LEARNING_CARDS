import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

openDatabase() async {
  var databasesPath = await getDatabasesPath();

  String path = join(databasesPath, 'en_tr_dct.db');
}
