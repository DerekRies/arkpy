from arkpy.ark import ArkCharacterSetting



def main():
  fp = 'data/SavedArksLocal/min.arkcharactersetting'
  # fp = 'data/SavedArksLocal/minandblack.arkcharactersetting'
  # fp = 'data/SavedArksLocal/maxandbrown.arkcharactersetting'
  # fp = 'data/SavedArksLocal/mini.arkcharactersetting'
  character = ArkCharacterSetting.from_file(fp)
  print character.character_setting


if __name__ == '__main__':
  main()