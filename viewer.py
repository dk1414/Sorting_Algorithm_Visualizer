
# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *

import random
import time



def bubble_sort(our_list):
    has_swapped = True

    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations - 1):
            yield [i,None]
            yield [i+1,None]
            if our_list[i] > our_list[i+1]:
                # Swap
                yield [i+1,i]
                yield [i,i+1]
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True

        num_of_iterations += 1


def insertion_sort(our_list):

        for step in range(1, len(our_list)):
            key = our_list[step]
            yield [step,None]
            j = step - 1

            while j >= 0 and key < our_list[j]:
                yield [j,None]
                yield [j, j + 1]
                our_list[j + 1] = our_list[j]

                j = j - 1


            our_list[j + 1] = key
            yield [None, j + 1]


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    yield [i,None]
    yield [l,None]
    if l < n and arr[i] < arr[l]:
        largest = l

    yield [largest,None]
    yield [r,None]
    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield [largest,i]
        yield [i,largest]
        yield from heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2, -1, -1):
        yield from heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        yield [0,i]
        yield [i,0]

        # Heapify root element
        yield from heapify(arr, i, 0)



def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    yield [high,None]

    for j in range(low, high):

        # If current element is smaller
        # than or equal to pivot
        yield [j,None]
        if arr[j] <= pivot:
            # increment index of
            # smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield [j,i]
            yield [i,j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield [high,i+1]
    yield [i+1,high]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = yield from partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        yield from quickSort(arr, low, pi - 1)

        yield from quickSort(arr, pi + 1, high)


def merge_inplace(arr, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        yield [mid,None]
        yield [start2,None]
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):

        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            yield [start,None]
            yield [start2,None]
            start += 1
        else:
            value = arr[start2]
            yield [start2,None]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                yield [index - 1,index]
                index -= 1

            arr[start] = value
            yield [None,start]

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1


'''
* l is for left index and r is right index of
the sub-array of arr to be sorted
'''


def mergeSort_inplace(arr, l, r):
    if (l < r):
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        yield from mergeSort_inplace(arr, l, m)
        yield from mergeSort_inplace(arr, m + 1, r)

        yield from merge_inplace(arr, l, m, r)


def cycleSort(array):
    writes = 0

    # Loop through the array to find cycles to rotate.
    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]
        yield [cycleStart,None]

        # Find where to put the item.
        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            yield [i,None]
            if array[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == array[pos]:
            yield [pos,None]
            pos += 1
        array[pos], item = item, array[pos]
        yield [None,pos]
        yield [pos,None]
        writes += 1

        # Rotate the rest of the cycle.
        while pos != cycleStart:

            # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(array)):
                yield [i,None]
                if array[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == array[pos]:
                yield [pos,None]
                pos += 1
            array[pos], item = item, array[pos]
            yield [None,pos]
            yield [pos,None]
            writes += 1

    return writes


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            yield [i,None]
            yield [i+1,None]
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                yield [i+1,i]
                yield [i,i+1]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end - 1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            yield [i,None]
            yield [i+1,None]
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                yield [i+1,i]
                yield [i,i+1]
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1


def shellSort(arr, n):
    # code here
    gap = n // 2

    while gap > 0:
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            i = j - gap  # This will keep help in maintain gap value

            while i >= 0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                yield [i + gap, None]
                yield [i, None]
                if arr[i + gap] > arr[i]:

                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                    yield [i, i + gap]
                    yield [i + gap, i]

                i = i - gap  # To check left side also
                # If the element present is greater than current element
            j += 1
        gap = gap // 2

class Model:

    def __init__(self,lst):
        self.lst = lst
        self.generator = None
        self.sorting = False
        self.writing = None
        self.reading = None
        self.size = len(self.lst)
        self.tick_speed = 300
        self.sorted = False


    def reset(self):
        self.lst = make_random_list(1,100,self.size)
        self.sorting = False
        self.reading = None
        self.writing = None
        self.sorted = False

    def change_size(self,num):
        cond = True
        if self.size == 40 and num < 0:
            cond = False
        elif self.size == 300 and num > 0:
            cond = False

        if cond:
            self.size += num
            self.reset()

    def change_tick_speed(self,num):
        cond = True
        if self.tick_speed == 10 and num < 0:
            cond = False
        elif self.tick_speed == 600 and num > 0:
            cond = False

        if cond:
            self.tick_speed += num

    def start_sort(self):
        self.sorting = True

    def advance(self):
        try:
            temp = next(self.generator)
            self.reading = temp[0]

            if temp[1] != None:
                self.writing = temp[1]
        except StopIteration:
            self.sorting = False
            self.reading = None
            self.writing = None
            self.sorted = True

    def bubble(self):
        self.generator = bubble_sort(self.lst)

    def insort(self):
        self.generator = insertion_sort(self.lst)

    def heap(self):
        self.generator = heapSort(self.lst)

    def merge(self):
        self.generator = mergeSort_inplace(self.lst,0,self.size-1)

    def quick(self):
        self.generator = quickSort(self.lst,0,self.size - 1)

    def cycle(self):
        self.generator = cycleSort(self.lst)

    def cocktail(self):
        self.generator = cocktailSort(self.lst)

    def shell(self):
        self.generator = shellSort(self.lst,self.size)





class Button:
    def __init__(self,screen,text,width,height,pos,pressed_func):

        self.screen = screen
        self.orig_pos = pos

        self.pressed = False
        self.pressed_func = pressed_func
        self.elevation = 6

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (200,200,200)

        self.font = pygame.font.SysFont('georgia', 20)

        self.top_rect_text = self.font.render(text, True, (0,0,0))

        self.top_text_rec = self.top_rect_text.get_rect()
        self.top_text_rec.center = (self.top_rect.center)

        self.bottom_rect = pygame.Rect(pos,(width,self.elevation))
        self.bottom_color = (150,150,150)


    def draw(self):

        self.top_rect.y = self.orig_pos[1] - self.elevation
        self.top_text_rec.center = self.top_rect.center



        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.elevation

        pygame.draw.rect(self.screen,self.bottom_color,self.bottom_rect,border_radius=10)
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius=10)
        self.screen.blit(self.top_rect_text, self.top_text_rec)

        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (100,100,100)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.elevation = 0
            elif self.pressed:
                self.pressed_func()
                self.pressed = False
                self.elevation = 6
        else:
            self.top_color = (200,200,200)
            self.elevation = 6







def make_random_list(start,end,size):
    lst = []

    for i in range(size):
        lst.append(random.randrange(start,end))

    return lst





def update(dt):


    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        # Handle other events as you wish.


def draw(screen,model,buttons):
    """
    Draw things to the window. Called once per frame.
    """

    screen.fill((255, 255, 255))  # Fill the screen with white

    rec_colors = [(100,100,100),(150,150,150),(200,200,200)]
    sorted_color = (0,225,0)

    side_pad = 200
    top_pad = 300

    #fonts
    medium_font = pygame.font.SysFont('georgia', 20)
    large_font =  pygame.font.SysFont('georgia', 32)

    #title text
    upper_text = large_font.render("Algorithm Viewer",True,(0,0,0))
    upper_text_rect = upper_text.get_rect()
    upper_text_rect.center = (screen.get_width()/2,32)
    screen.blit(upper_text,upper_text_rect)


    #list size text
    size_text = medium_font.render(f"List Size: {model.size}",True,(0,0,0))
    size_text_rect = size_text.get_rect()
    size_text_rect.center = (screen.get_width()/2 - 200,100)
    screen.blit(size_text,size_text_rect)

    #tick speed text
    speed_text = medium_font.render(f"Tick Speed: {model.tick_speed}",True,(0,0,0))
    speed_text_rect = speed_text.get_rect()
    speed_text_rect.center = (screen.get_width()/2 + 200,100)
    screen.blit(speed_text,speed_text_rect)


    if model.generator != None and model.sorting:
        model.advance()


    mn = min(model.lst)
    mx = max(model.lst)
    range = mx - mn

    pixel_size = round((screen.get_height() - top_pad) / range)
    width = (screen.get_width() - side_pad) / model.size


    # Redraw screen here.
    for i,r in enumerate(model.lst):


        current_color = rec_colors[i % 3]

        if model.reading == i:
            current_color = (225,0,0)

        if model.writing == i:
            current_color = (0,255,0)




        pygame.draw.rect(screen,current_color,(i*width + side_pad/2,(screen.get_height()-top_pad/2) - r*pixel_size,width,r*pixel_size))


    for button in buttons:
        button.draw()

    #sorted animation
    if model.sorted:
        for j, k in enumerate(model.lst):
            pygame.draw.rect(screen, sorted_color, (
            j * width + side_pad / 2, (screen.get_height() - top_pad / 2) - k * pixel_size, width, k * pixel_size))

            for button in buttons:
                button.draw()

            pygame.display.flip()
            update(True)
            time.sleep(0.005)
        model.sorted = False



    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def bubble_button(m:Model):
    m.bubble()
    m.start_sort()

def insertion_button(m:Model):
    m.insort()
    m.start_sort()

def heap_button(m:Model):
    m.heap()
    m.start_sort()

def merge_button(m:Model):
    m.merge()
    m.start_sort()

def quick_button(m:Model):
    m.quick()
    m.start_sort()

def cycle_button(m:Model):
    m.cycle()
    m.start_sort()

def cocktail_button(m:Model):
    m.cocktail()
    m.start_sort()

def shell_button(m:Model):
    m.shell()
    m.start_sort()

def runPyGame():
    # Initialise PyGame.
    pygame.init()



    m = Model(make_random_list(1,100,150))
    buttons_list = []

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = m.tick_speed
    fpsClock = pygame.time.Clock()

    # Set up the window.
    width, height = 1200,800


    screen = pygame.display.set_mode((width, height))

    pygame_icon = pygame.image.load('bar_graph.png')
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption("AlgoViewer")



    reset_button = Button(screen,"Reset",100,50,(screen.get_width()/2 - 50,80),lambda:m.reset())
    buttons_list.append(reset_button)

    b_button = Button(screen,"Bubble",100,50,(100,700),lambda:bubble_button(m))
    buttons_list.append(b_button)

    insert_button = Button(screen,"Insertion",100,50,(225,700),lambda:insertion_button(m))
    buttons_list.append(insert_button)

    h_button = Button(screen,"HeapSort",100,50,(350,700),lambda:heap_button(m))
    buttons_list.append(h_button)

    m_button = Button(screen,"MergeSort",100,50,(475,700),lambda:merge_button(m))
    buttons_list.append(m_button)

    q_button = Button(screen,"QuickSort",100,50,(600,700),lambda:quick_button(m))
    buttons_list.append(q_button)

    c_button = Button(screen,"CycleSort",100,50,(725,700),lambda:cycle_button(m))
    buttons_list.append(c_button)

    ck_button = Button(screen,"Cocktail",100,50,(850,700),lambda:cocktail_button(m))
    buttons_list.append(ck_button)

    sh_button = Button(screen,"ShellSort",100,50,(975,700),lambda:shell_button(m))
    buttons_list.append(sh_button)


    increment_button = Button(screen,">",25,20,(screen.get_width()/2 -135,95),lambda:m.change_size(5))
    buttons_list.append(increment_button)

    decrement_button = Button(screen,"<",25,20,(screen.get_width()/2 - 288,95),lambda:m.change_size(-5))
    buttons_list.append(decrement_button)

    inc_speed_button = Button(screen,">",25,20,(screen.get_width()/2 + 275,95),lambda:m.change_tick_speed(5))
    buttons_list.append(inc_speed_button)

    dec_speed_button = Button(screen, "<", 25, 20, (screen.get_width() / 2 + 100, 95), lambda: m.change_tick_speed(-5))
    buttons_list.append(dec_speed_button)


    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Main game loop.
    dt = 1 / fps * 1000 # dt is the time since last frame.
    while True:  # Loop forever!
        fps = m.tick_speed
        update(dt)  # You can update/draw here, I've just moved the code for neatness.
        draw(screen,m,buttons_list)

        dt = fpsClock.tick(fps)

if __name__ == "__main__":
    runPyGame()