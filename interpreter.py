import sys


def show(img_name):
        img_dict = {
                        'zombie': '',
                                'santa': '',
                                        'default': ''
                                            }
            print('Showing %s...' % img_name)
                # TODO: load new image
                    print('Done!') 
                    def color(c):
                            # TODO: set all pixels a color c
                                print('Making all lights turn %s...' % c)
                                    print('Done!') 
                                    cmd_dict = {
                                                'show': show,
                                                    'color': color,
                                                        'end': lambda x: sys.exit(0)
                                                        }                                     cmd = ''
                                    while cmd != 'end':
                                            try:
                                                        sys.stdout.write('> ')
                                                                x = input()
                                                                        parts = x.split(' ')
                                                                                
                                                                                        if len(parts) == 2:
                                                                                                                                                                cmd_dict[parts[0]](parts[1])
                                                                                                                                                                        else:
                            cmd_dict[parts[0]]()
                                except KeyboardInterrupt as ki:
                                            print('\nStopping!')
                                                    sys.exit(0)
                                                        except ValueError as ve:
                                                                    print('Whoops, try again!')
                                                                            # TODO: print specific message about missing argument
                                                                                # except KeyError as ke:
                                                                                    
                                                                                        except Exception as ex:
                                                                                                    raise ex
                                                                                                        print('Whoops, I don\'t know that command!')
