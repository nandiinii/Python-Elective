stud = {}
stud={
    47:"P Nandini",
    59:"Sneha",
    60:"Sona",
    53:"Niranjana",
    49:"Navya"
}
studlist=list(stud.items())
sortrno=sorted(studlist)
print(sortrno)
sortname=sorted(stud.items(),key=lambda x:x[1])
print(sortname)
stud1={
    47:{'name':"Nandini",'mark':75},
    48:{'name':"Nandu",'mark':87},
    49:{'name':"Navya P S",'mark':95},
    50:{'name':"Navya V",'mark':90},
    51:{'name':"Netanya",'mark':89},
}
print(stud1)













