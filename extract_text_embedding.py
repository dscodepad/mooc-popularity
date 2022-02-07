from nltk.corpus import wordnet
import json

def prepare_text():
    file = "course-text-data.csv"
    title_texts, objectives_text, prerequisite_texts, description_texts, target_audience_texts = [], [], [], [], []
    count = 0
    with open(file, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # skip the headers
        for row in reader:
            # print(row)
            ID = row[1]
            if ID in no_en:
                continue
            count_title = int(row[2])
            count_objective = int(row[3])
            count_prerequisite = int(row[4])
            count_description = int(row[5])
            count_target_audience = int(row[6])

            title_headline = row[7]
            objectives = row[8]
            prerequisite = row[9]
            description = row[10]
            target_audience = row[11]
            count += 1

            title_texts.append([ID, title_headline, count_title])
            objectives_text.append([ID, objectives, count_objective])
            prerequisite_texts.append([ID, prerequisite, count_prerequisite])
            description_texts.append([ID, description, count_description])
            target_audience_texts.append([ID, target_audience, count_target_audience])

            if count % 1000 == 0:
                print("count ", count)

    title_texts.sort(key=lambda x: x[2])
    objectives_text.sort(key=lambda x: x[2])
    prerequisite_texts.sort(key=lambda x: x[2])
    description_texts.sort(key=lambda x: x[2])
    target_audience_texts.sort(key=lambda x: x[2])

    print("len courses added: ", len(title_texts))

    return title_texts, objectives_text, prerequisite_texts, description_texts, target_audience_texts

title_texts, objectives_text, prerequisite_texts, description_texts, target_audience_texts = prepare_text()

def extracte_embedding():
    # extract embeddings of the title-headline, objective, prerequisite, description, and target audience, save to json file.
    bc = BertClient()
    courseID_bytitle = [x[0] for x in title_texts]
    title_content = [x[1] for x in title_texts]
    #title_content_part = title_content[0:20]

    # title_headline_embedding = bc.encode(title_content)
    #
    # print(title_headline_embedding.shape)
    # print(type(title_headline_embedding))
    # #print(title_headline_embedding)
    #
    #
    # # title_headline_embedding_wID = zip(courseID_bytitle,title_headline_embedding)
    # # print(title_headline_embedding_wID)
    #
    # course_title_embedding = {}
    # for k in range(len(title_headline_embedding)):
    #     courseID = courseID_bytitle[k]
    #     title_vec = title_headline_embedding[k]
    #     course_title_embedding[courseID] = title_vec.tolist()
    # print(len(course_title_embedding))
    # write_dict2json(course_title_embedding,"course_title_embedding.json")


    # courseID_byobjective = [x[0] for x in objectives_text]
    # objective_content = [x[1] for x in objectives_text]
    #
    # objectives_embedding = bc.encode(objective_content)
    #
    # course_objectives_embedding = {}
    # for k in range(len(objectives_embedding)):
    #     courseID = courseID_byobjective[k]
    #     objective_vec = objectives_embedding[k]
    #     course_objectives_embedding[courseID] = objective_vec.tolist()
    # print(len(course_title_embedding))
    # write_dict2json(course_objectives_embedding, "course_objectives_embedding.json")


    courseID_byprerequisite = [x[0] for x in prerequisite_texts]
    prerequisite_content = [x[1] for x in prerequisite_texts]

    prerequisite_embedding = bc.encode(prerequisite_content)

    course_prerequisite_embedding = {}
    for k in range(len(prerequisite_embedding)):
        courseID = courseID_byprerequisite[k]
        prerequisite_vec = prerequisite_embedding[k]
        course_prerequisite_embedding[courseID] = prerequisite_vec.tolist()
    print(len(course_prerequisite_embedding))
    write_dict2json(course_prerequisite_embedding, "course_prerequisite_embedding.json")


    courseID_bydescription = [x[0] for x in description_texts]
    description_content = [x[1] for x in description_texts]

    description_embedding = bc.encode(description_content)
    course_description_embedding = {}
    for k in range(len(description_embedding)):
        courseID = courseID_bydescription[k]
        description_vec = description_embedding[k]
        course_description_embedding[courseID] = description_vec.tolist()
    print(len(course_description_embedding))
    write_dict2json(course_description_embedding, "course_description_embedding.json")


    courseID_bytarget = [x[0] for x in target_audience_texts]
    target_audience_content = [x[1] for x in target_audience_texts]

    target_audience_embedding = bc.encode(target_audience_content)
    course_target_audience_embedding = {}
    for k in range(len(target_audience_embedding)):
        courseID = courseID_bytarget[k]
        target_audience_vec = target_audience_embedding[k]
        course_target_audience_embedding[courseID] = target_audience_vec.tolist()
    print(len(course_target_audience_embedding))
    write_dict2json(course_target_audience_embedding, "course_target_audience_embedding.json")

extract_embedding()