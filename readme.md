# proto-typist


Generate proto from proto so that you don't need to write it by yourself.


## `service_to_messages.py`

Generate request/response messages from service definition.

Input:
```
service OrgService {
  // Orgs
  rpc CreateOrg(CreateOrgRequest) returns (CreateOrgResponse) {}
  rpc GetOrg(GetOrgRequest) returns (GetOrgResponse) {}
  rpc ListOrgs(ListOrgsRequest) returns (ListOrgsResponse) {}
  rpc ActivateOrg(ActivateOrgRequest) returns (ActivateOrgResponse) {}
  rpc DeactivateOrg(DeactivateOrgRequest) returns (DeactivateOrgResponse) {}
  rpc UpdateOrgUsers(UpdateOrgUsersRequest) returns (UpdateOrgUsersResponse) {}
}
```

Output:
```
message CreateOrgRequest {
}

message CreateOrgResponse {
}

message GetOrgRequest {
}

message GetOrgResponse {
}

...
```
