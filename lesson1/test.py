MainDic={
"Anton": {"city": "Moscow", "temperature":25, "wind":"eastern"},
"Vasya": {"city":"Moscow","temperature":30,"wind":"western"},
"Petya": {"city":"Moscow","temperature":30,"wind":"western"},
}
print(MainDic.get(input('Who are you?')))
