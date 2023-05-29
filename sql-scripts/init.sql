CREATE TABLE IF NOT EXISTS kubernetes (
  kobj VARCHAR(255) NOT NULL,
  kdef TEXT NOT NULL,
  kcommand TEXT NOT NULL
);

-- Insert rows into kubernetes table if they don't exist
INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'pod', 'group of one or more containers', 'kubectl get po'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'pod');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'deployment', 'enables declarative updates for Pods and ReplicaSets', 'kubectl get deploy'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'deployment');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'service', 'abstraction to helps exposing groups of Pods over a network', 'kubectl get svc'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'service');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'statefulset', 'set of pods with consistent identities e.g. Storage, Network', 'kubectl get sts'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'statefulset');
