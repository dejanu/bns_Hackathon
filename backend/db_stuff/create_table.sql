-- create table for kubernetes objects: kobj, kdef, kcommand columns

CREATE TABLE kubernetes (
  kobj VARCHAR(255) NOT NULL,
  kdef TEXT NOT NULL,
  kcommand TEXT NOT NULL
);

-- insert rows into kubernetes table
INSERT INTO kubernetes (kobj, kdef, kcommand) VALUES ('pod', 'group of one or more containers', 'kubectl get po');
INSERT INTO kubernetes (kobj, kdef, kcommand) VALUES ('deployment', 'enables declarative updates for Pods and ReplicaSets', 'kubectl get deploy');
INSERT INTO kubernetes (kobj, kdef, kcommand) VALUES ('service', 'abstraction to helps exposing groups of Pods over a network', 'kubectl get svc');
INSERT INTO kubernetes (kobj, kdef, kcommand) VALUES ('statefulset', 'set of pods with consistent identities e.g. Storage,Network', 'kubectl get sts');