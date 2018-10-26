def sayhello (name, school="ADNU"):
    print("Hello, {} from {}.".format(name, school))

sayhello("Glenn")
sayhello("Glenn","ADNU")
sayhello(name="Glenn", school="PNHS")
sayhello(school="PCS", name="Glenn")