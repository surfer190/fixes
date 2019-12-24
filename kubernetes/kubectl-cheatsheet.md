## Common Kubectl Commands

List API Resources available

    $ kubectl api-resources

    NAME                              SHORTNAMES      APIGROUP                       NAMESPACED   KIND
    bindings                                                                         true         Binding
    componentstatuses                 cs                                             false        ComponentStatus
    configmaps                        cm                                             true         ConfigMap
    endpoints                         ep                                             true         Endpoints
    events                            ev                                             true         Event
    limitranges                       limits                                         true         LimitRange
    namespaces                        ns                                             false        Namespace
    nodes                             no                                             false        Node
    persistentvolumeclaims            pvc                                            true         PersistentVolumeClaim
    persistentvolumes                 pv                                             false        PersistentVolume
    pods                              po                                             true         Pod
    podtemplates                                                                     true         PodTemplate
    replicationcontrollers            rc                                             true         ReplicationController
    resourcequotas                    quota                                          true         ResourceQuota
    secrets                                                                          true         Secret
    serviceaccounts                   sa                                             true         ServiceAccount
    services                          svc                                            true         Service
    mutatingwebhookconfigurations                     admissionregistration.k8s.io   false        MutatingWebhookConfiguration
    validatingwebhookconfigurations                   admissionregistration.k8s.io   false        ValidatingWebhookConfiguration
    customresourcedefinitions         crd,crds        apiextensions.k8s.io           false        CustomResourceDefinition
    apiservices                                       apiregistration.k8s.io         false        APIService
    controllerrevisions                               apps                           true         ControllerRevision
    daemonsets                        ds              apps                           true         DaemonSet
    deployments                       deploy          apps                           true         Deployment
    replicasets                       rs              apps                           true         ReplicaSet
    statefulsets                      sts             apps                           true         StatefulSet
    tokenreviews                                      authentication.k8s.io          false        TokenReview
    localsubjectaccessreviews                         authorization.k8s.io           true         LocalSubjectAccessReview
    selfsubjectaccessreviews                          authorization.k8s.io           false        SelfSubjectAccessReview
    selfsubjectrulesreviews                           authorization.k8s.io           false        SelfSubjectRulesReview
    subjectaccessreviews                              authorization.k8s.io           false        SubjectAccessReview
    horizontalpodautoscalers          hpa             autoscaling                    true         HorizontalPodAutoscaler
    cronjobs                          cj              batch                          true         CronJob
    jobs                                              batch                          true         Job
    certificatesigningrequests        csr             certificates.k8s.io            false        CertificateSigningRequest
    ingressroutes                                     contour.heptio.com             true         IngressRoute
    tlscertificatedelegations                         contour.heptio.com             true         TLSCertificateDelegation
    leases                                            coordination.k8s.io            true         Lease
    events                            ev              events.k8s.io                  true         Event
    ingresses                         ing             extensions                     true         Ingress
    ingresses                         ing             networking.k8s.io              true         Ingress
    networkpolicies                   netpol          networking.k8s.io              true         NetworkPolicy
    runtimeclasses                                    node.k8s.io                    false        RuntimeClass
    poddisruptionbudgets              pdb             policy                         true         PodDisruptionBudget
    podsecuritypolicies               psp             policy                         false        PodSecurityPolicy
    httpproxies                       proxy,proxies   projectcontour.io              true         HTTPProxy
    tlscertificatedelegations         tlscerts        projectcontour.io              true         TLSCertificateDelegation
    clusterrolebindings                               rbac.authorization.k8s.io      false        ClusterRoleBinding
    clusterroles                                      rbac.authorization.k8s.io      false        ClusterRole
    rolebindings                                      rbac.authorization.k8s.io      true         RoleBinding
    roles                                             rbac.authorization.k8s.io      true         Role
    priorityclasses                   pc              scheduling.k8s.io              false        PriorityClass
    csidrivers                                        storage.k8s.io                 false        CSIDriver
    csinodes                                          storage.k8s.io                 false        CSINode
    storageclasses                    sc              storage.k8s.io                 false        StorageClass
    volumeattachments                                 storage.k8s.io                 false        VolumeAttachment