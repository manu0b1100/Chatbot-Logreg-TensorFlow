# str = ""
#     s = Skill.objects.all()
#     cv = CountVectorizer()
#     for i in s:
#         str = str + i.name.replace(" ","") + " "
#
#
#     cv.fit([str])
#     joblib.dump(cv,'chat_ml/Data/skillvector.pkl')
#     cv=joblib.load('chat_ml/Data/skillvector.pkl')
#     cvt = cv.transform(["Java webdevelopment"])
#
#     print(cv.get_feature_names())
#     print(cv.inverse_transform(cvt.toarray()))



