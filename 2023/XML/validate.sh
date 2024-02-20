# We are going to validate the DTDs of:
# posthistory
# posts
# users
# votes

xmllint --noout --dtdvalid ./schemas/posthistory.dtd ./source/PostHistory.xml
xmllint --noout --dtdvalid ./schemas/posts.dtd ./source/Posts.xml
xmllint --noout --dtdvalid ./schemas/users.dtd ./source/Users.xml
xmllint --noout --dtdvalid ./schemas/votes.dtd ./source/Votes.xml

# We are going to validate the XSDs of:
# badges
# comments
# postlinks
# tags

xmllint --noout --schema ./schemas/badges.xsd ./source/Badges.xml
xmllint --noout --schema ./schemas/comments.xsd ./source/Comments.xml
xmllint --noout --schema ./schemas/postlinks.xsd ./source/PostLinks.xml
xmllint --noout --schema ./schemas/tags.xsd ./source/Tags.xml
