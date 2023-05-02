-- create table for kubernetes objects: kobj, kdef, kcommand columns

CREATE TABLE kubernetes (
  kobj VARCHAR(255) NOT NULL,
  kdef TEXT NOT NULL,
  kcommand TEXT NOT NULL
);

-- insert one row into kubernetes table
INSERT INTO kubernetes (kobj, kdef, kcommand) VALUES ('pod', 'group of one or more containers', 'kubectl get po');