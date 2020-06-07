import time
from tqdm import tqdm
from rich_fmt import rich_print as print
from rich_fmt import rich_fmt, base_colors

def print_demo():
    print('\n     Normal: ', end='')
    for color in base_colors:
        print('[%s]Python[/%s] '%(color, color), end='')

    print('\n       Bold: ', end='')
    for color in base_colors:
        print('[b_%s]Python[/b_%s] '%(color, color), end='')

    print('\n        Dim: ', end='')
    for color in base_colors:
        print('[%s][dim]Python[/dim][/%s] '%(color, color), end='')

    print('\n  Underline: ', end='')
    for color in base_colors:
        print('[u_%s]Python[/u_%s] '%(color, color), end='')
    
    print('\n Italicized: ', end='')
    for color in base_colors:
        print('[i_%s]Python[/i_%s] '%(color, color), end='')
    
    print('\n      Blink: ', end='')
    for color in base_colors:
        print('[%s][blink]Python[/blink][/%s] '%(color, color), end='')
    
    print('\n    Inverse: ', end='')
    for color in base_colors:
        print('[%s][inv]Python[/inv][/%s] '%(color, color), end='')
    
    print('\n')

print_demo()

print('\n[u][b]Basic styles[/u][/b]')
print(' - Bold       [b]Hello[/b]')
print(' - Underline  [u]Hello[/u]')
print(' - Italicized [i]Hello[/i]')
print(' - Inversed   [inv]Hello[/inv]')
print(' - Blink      [blink]Hello[/blink]')
print(' - Dim        [dim]Hello[/dim]')

print('\n[u][b]Colors[/u][/b]')
print(' - Colors               [gray]gray[/gray], [red]red[/red], [green]green[/green], [yellow]yellow[/yellow], [blue]blue[/blue], [magenta]magenta[/magenta], [cyan]cyan[/cyan], [white]white[/white]')
print(' - Equal bbcode         [green]AAA[/green] [color=green]AAA[/color]')
print(' - Style Shortcut       [yellow][u]AAA[/u][/yellow] [u_yellow]AAA[/u_yellow]')
print(' - 3 types of Shortcuts [b_blue]AAA[/b_blue] [u_blue]AAA[/u_blue] [i_blue]AAA[/i_blue]')

print('\n[u][b]Progress bar[/u][/b]')
with tqdm(total=10, leave=True, dynamic_ncols=True) as pbar:
    for i in range(10):
        pbar.set_description(rich_fmt('Progress: i = [b_yellow]%d[/b_yellow], i**2 = [u_green]%d[/u_green]'%(i, i**2)))
        pbar.update(1)
        time.sleep(0.5)
