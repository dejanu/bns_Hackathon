CREATE TABLE IF NOT EXISTS kubernetes (
  kobj VARCHAR(255) NOT NULL,
  kdef TEXT NOT NULL,
  kcommand TEXT NOT NULL
);

-- Insert rows into kubernetes table if they don't exist
INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'pod', 'group of one or more containers with shared storage and network resources', '$ kubectl get po'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'pod');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'deployment', 'enables declarative updates for Pods and ReplicaSets', '$ kubectl get deploy'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'deployment');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'replicaset', 'maintains a stable set of replica Pods running at any given time', '$ kubectl get rs'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'replicaset');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'service', 'abstraction that helps exposing groups of Pods over a network', '$ kubectl get svc'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'service');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'statefulset', 'set of pods with consistent identities e.g. Storage, Network', '$ kubectl get sts'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'statefulset');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'persistentvolume ', 'storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes', '$ kubectl get pv'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'persistentvolume');

INSERT INTO kubernetes (kobj, kdef, kcommand)
SELECT 'persistentvolumeclaim  ', 'request for storage by a user, requesting specific size and access mode ReadWriteOnce, ReadOnlyMany or ReadWriteMany', '$ kubectl get pvc'
WHERE NOT EXISTS (SELECT 1 FROM kubernetes WHERE kobj = 'persistentvolumeclaim');