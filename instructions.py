

def check_for_txt():
    '''
    Check if there's an accompanying .txt file which tells us
    how the user wants the image animated
    Commands available are:
    NNNN speed S.SSS
      Set the scroll speed (in seconds)
      Example: 0000 speed 0.150
      At position zero (first position), set the speed to 150ms
    NNNN hold S.SSS
      Hold the frame still (in seconds)
      Example: 0011 hold 2.300
      At position 11, keep the image still for 2.3 seconds
    NNNN-PPPP flip S.SSS
      Animate MATRIX_WIDTH frames, like a flipbook
      with a speed of S.SSS seconds between each frame
      Example: 0014-0049 flip 0.100
      From position 14, animate with 100ms between frames
      until you reach or go past position 49
      Note that this will jump positions MATRIX_WIDTH at a time
      Takes a bit of getting used to - experiment
    NNNN jump PPPP
      Jump to position PPPP
      Example: 0001 jump 0200
      At position 1, jump to position 200
      Useful for debugging only - the image will loop anyway
    '''
    try:
        with open(sys.argv[2], 'r') as f:
            return f.read()
    except:
        return ''

def run_text_instructions(txt_idx, txt_lines, i, wait_len):
    inc = 1
    this_sleep = wait_len
    if txt_idx < len(txt_lines):
        match = re.search(
            r"^(?P<start>\s*\d+)(-(?P<finish>\d+))?\s+((?P<command>\S+)(\s+(?P<param>\d+(\.\d+)?))?)$",
            txt_lines[txt_idx],
            re.M | re.I,
        )
        if match:
            print("Found valid command line %d:\n%s" % (txt_idx, txt_lines[txt_idx]))
            st = int(match.group("start"))
            fi = st
            print("Current pixel %05d start %05d finish %05d" % (i, st, fi))
            if match.group("finish"):
                fi = int(match.group("finish"))
            if i >= st and txt_idx <= fi:
                if match.group("command").lower() == "speed":
                    this_sleep = float(match.group("param"))
                    print("Position %d : Set speed to %.3f secs per frame" % (
                        i,
                        this_sleep,
                    ))
                elif match.group("command").lower() == "flip":
                    this_sleep = float(match.group("param"))
                    inc = MATRIX_WIDTH
                    print("Position %d: Flip for %.3f secs" % (i, this_sleep))
                elif match.group("command").lower() == "hold":
                    this_sleep = float(match.group("param"))
                    print("Position %d: Hold for %.3f secs" % (i, this_sleep))
                elif match.group("command").lower() == "jump":
                    print("Position %d: Jump to position %s" % (
                        i,
                        match.group("param"),
                    ))
                    x = int(match.group("param"))
                    inc = 0
            # Move to the next line of the text file
            # only if we have completed all pixels in range
            if i >= fi:
                txt_idx += 1
        else:
            print("Found INVALID command line %d:\n%s" % (txt_idx, txt_lines[txt_idx]))
            txt_idx +=  1
    return inc, txt_idx, this_sleep

