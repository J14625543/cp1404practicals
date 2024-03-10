FILENAME = "subject_data.txt"


def main():
    subjects = get_subjects()
    display_subjects(subjects)


def get_subjects():
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        subject.append(parts)
    input_file.close()
    return subject