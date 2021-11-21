import 'package:json_annotation/json_annotation.dart';

class Word {
  String word;
  String? meaning;
  String? example;
  String? synonym;
  String? antonym;
  String? wordType;
  String? wordClass;
  String? wordFamily;
  String? wordGroup;
  String? wordOrigin;
  String? wordMeaning;
  String? wordExample;
  String? wordSynonym;
  String? wordAntonym;

  Word({
    required this.word,
    this.meaning,
    this.example,
    this.synonym,
    this.antonym,
    this.wordType,
    this.wordClass,
    this.wordFamily,
    this.wordGroup,
    this.wordOrigin,
    this.wordMeaning,
    this.wordExample,
    this.wordSynonym,
    this.wordAntonym,
  });
}
