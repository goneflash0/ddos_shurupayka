from pystyle import Colors, Box, Write, Center, Colorate
import pystyle

color_code = {
    "reset": "\033[0m",
    "underline": "\033[04m",
    "green": "\033[32m",
    "yellow": "\033[93m",
    "red": "\033[31m",
    "cyan": "\033[36m",
    "bold": "\033[01m",
    "url_l": "\033[36m",
    "li_g": "\033[92m",
    "f_cl": "\033[0m",
    "dark": "\033[90m",
    "purple": "\033[95m",
    "blue": "\033[94m"
}
banner = ('''
                              oooooooooo.   oooooooooo.     .oooooo.    .oooooo..o                                           
                              `888'   `Y8b  `888'   `Y8b   d8P'  `Y8b  d8P'    `Y8                                           
                               888      888  888      888 888      888 Y88bo.                                                
                               888      888  888      888 888      888  `"Y8888o.                                            
                               888      888  888      888 888      888      `"Y88b                                           
                               888     d88'  888     d88' `88b    d88' oo     .d8P                                           
                              o888bood8P'   o888bood8P'    `Y8bood8P'  8""88888P'                                            
                                                                                                                             
                                                                                                                             
                                                                                                                             
oooooo   oooooo     oooo oooooooooooo ooooo      ooo  .oooooo..o ooooo  oooooooooooo  oooooooooooo oooooooooooo ooooooooo.   
 `888.    `888.     .8'  `888'     `8 `888b.     `8' d8P'    `Y8 `888' d'""""""d888' d'""""""d888' `888'     `8 `888   `Y88. 
  `888.   .8888.   .8'    888          8 `88b.    8  Y88bo.       888        .888P         .888P    888          888   .d88' 
   `888  .8'`888. .8'     888oooo8     8   `88b.  8   `"Y8888o.   888       d888'         d888'     888oooo8     888ooo88P'  
    `888.8'  `888.8'      888    "     8     `88b.8       `"Y88b  888     .888P         .888P       888    "     888`88b.    
     `888'    `888'       888       o  8       `888  oo     .d8P  888    d888'    .P   d888'    .P  888       o  888  `88b.  
      `8'      `8'       o888ooooood8 o8o        `8  8""88888P'  o888o .8888888888P  .8888888888P  o888ooooood8 o888o  o888o
''')
colored_banner = Colorate.Diagonal(Colors.black_to_white, banner)
print(colored_banner)

print(f'''
{color_code['dark']}{'creator: @Xxxwhyxx — 死| ᴄᴀᴛ ɴᴏɪʀ'.center(110)}
{'channel: @Wensizzer'.center(110)}
{'version: Ddos'.center(110)}{color_code['reset']}
''')
