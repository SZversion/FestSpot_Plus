import { useQuery } from "@tanstack/react-query";
import React from "react";
import { reqPrincipal } from "../../api/authApi";

function usePrincipalQuery(props) {
  return useQuery({
    queryKey: ["principal"],
    queryFn: async () => await reqPrincipal(),
    staleTime: 1000 * 60 * 30,
    gcTime: 1000 * 60 * 30,
  });
}

export default usePrincipalQuery;
