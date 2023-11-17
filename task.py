import pandas as pd

after = pd.read_csv('student_after_score.csv', usecols=[1])
before = pd.read_csv('student_before_score.csv', usecols=[1])
group = pd.read_csv('student_group.csv', usecols=[1])
mapping = {'course': True, 'no_course': False}
group = group.replace({'group': mapping})

countOfPupils = 0
withoutCourse = 0
withCourse = 0
for i in range(len(group)):
    personProgress = after['after_score'][i]-before['before_score'][i]
    if(group['group'][i]):
        countOfPupils += 1
        withCourse += personProgress
    else:
        withoutCourse += personProgress


withCourse = float(withCourse / countOfPupils)
withoutCourse = float(withoutCourse / (len(group)+1 - countOfPupils))

print(f'Средний прогресс составляет {withCourse} для учеников, которые были на курсах и {withoutCourse} для тех, кто не был')
