print("""
 ██████╗  ██████╗███████╗██████╗ 
██╔════╝ ██╔════╝╚════██║██╔══██╗
███████╗ ██║  ███╗   ██╔╝██████╔╝
██╔═══██╗██║   ██║  ██╔╝ ██╔══██╗
╚██████╔╝╚██████╔╝  ██║  ██║  ██║
 ╚═════╝  ╚═════╝   ╚═╝  ╚═╝  ╚═╝
                                 

INSTA ((((6G7R_here))))

""")




user = open("user.txt","r").read().splitlines()
password = open("pass.txt","r").read().splitlines()
with open("combo.txt", "a") as mix: 
  for username, password in zip(user, password):
    mix.write(f"{username} : {password}\n")
    mix.close
    
    
    print("done !")
