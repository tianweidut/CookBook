#coding: utf-8


class SchedulerShutdown(SystemExit):
    code = 1
    message = 'dpark.SchedulerShutdown'


def a():
    print("start test")

    raise SchedulerShutdown("test")

def main():
    try:
        a()
    except Exception as e:
        print(e)
    except SystemExit as e2:
        print(e2)
        print(e2.message)
        print(str(e2.__class__))
        import pdb; pdb.set_trace()
        print('SchedulerShutdown' in str(e2.__class__))


if __name__ == "__main__":
    main()
