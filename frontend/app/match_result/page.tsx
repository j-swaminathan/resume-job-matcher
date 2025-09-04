"use client"

import { useEffect, useState } from "react"
import { Box, Typography, Button, List, ListItem } from "@mui/material"
import { useRouter } from "next/navigation"

export default function MatchResultPage() {
  const [result, setResult] = useState<any>(null)
  const router = useRouter()

  useEffect(() => {
    const data = sessionStorage.getItem("matchResult")
    if (data) setResult(JSON.parse(data))
  }, [])

  if (!result) return <Typography>Loading... </Typography>

  return (
    <Box sx={{ maxWidth: 500, mx: "auto", mt: 6 }}>
      <Typography variant="h4" gutterBottom textAlign="center">
        Match Result
      </Typography>

      <Box sx={{ p: 3, border: "1px solid #ddd", borderRadius: 2, mb: 2 }}>
        <Typography variant="h6">Score: {result.score}%</Typography>
        <Typography variant="subtitle1">Model: {result.model}</Typography>
      </Box>

      {result.keywords && result.keywords.length > 0 && (
        <Box sx={{ p: 3, border: "1px solid #ddd", borderRadius: 2, mb: 2 }}>
          <Typography variant="subtitle1">Top Keywords:</Typography>
          <List>
            {result.keywords.map((kw: string, idx: number) => (
              <ListItem key={idx}>{kw}</ListItem>
            ))}
          </List>
        </Box>
      )}

      <Button variant="contained" fullWidth onClick={() => router.back()}>
        ⬅ Back
      </Button>
    </Box>
  )
}
