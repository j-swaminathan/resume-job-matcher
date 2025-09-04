
"use client"
import { useState } from "react"
import { Button, Box, Select, MenuItem, Typography } from "@mui/material"
import FileUpload from "../components/FileUpload"
import { useRouter } from "next/navigation"

export default function Home() {
  const [resume, setResume] = useState<File | null>(null)
  const [jobFile, setJobFile] = useState<File | null>(null)
  const [model, setModel] = useState("tfidf")
  const router = useRouter()

  const handleSubmit = async () => {
    if (!resume || !jobFile) {
      alert("Please upload both files")
      return
    }

    const formData = new FormData()
    formData.append("resume", resume)
    formData.append("job_desc", jobFile)
    formData.append("model", model)

    const res = await fetch("http://127.0.0.1:8000/match/", {
      method: "POST",
      body: formData,
    })

    const data = await res.json()
    sessionStorage.setItem("matchResult", JSON.stringify(data))

    router.push("/match_result")
  }

  return (
    <Box sx={{ maxWidth: 500, mx: "auto", mt: 6 }}>
      <Typography variant="h4" textAlign="center" gutterBottom>
        📄 Resume Matcher
      </Typography>

      <FileUpload label="Upload Resume (PDF)" onFileSelect={setResume} accept=".pdf" />
      <FileUpload label="Upload Job Description (TXT)" onFileSelect={setJobFile} accept=".txt" />

      <Select fullWidth value={model} onChange={(e) => setModel(e.target.value)} sx={{ mb: 2 }}>
        <MenuItem value="tfidf">TF-IDF</MenuItem>
        <MenuItem value="embeddings">Embeddings</MenuItem>
      </Select>

      <Button variant="contained" fullWidth onClick={handleSubmit}>
        Find Score
      </Button>
    </Box>
  )
}

