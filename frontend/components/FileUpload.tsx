"use client"

import { useDropzone } from "react-dropzone"
import { Box, Typography, Paper } from "@mui/material"

interface FileUploadProps {
  label: string
  onFileSelect: (file: File) => void
  accept: string
}

export default function FileUpload({ label, onFileSelect, accept }: FileUploadProps) {
  const { getRootProps, getInputProps, acceptedFiles } = useDropzone({
    accept: { [accept]: [] },
    maxFiles: 1,
    onDrop: (files) => {
      onFileSelect(files[0])
    },
  })

  return (
    <Box className="mb-4">
      <Typography variant="subtitle1" gutterBottom>
        {label}
      </Typography>
      <Paper
        {...getRootProps()}
        sx={{
          p: 2,
          border: "2px dashed #999",
          textAlign: "center",
          cursor: "pointer",
          bgcolor: "#f9f9f9",
        }}
      >
        <input {...getInputProps()} />
        {acceptedFiles.length > 0 ? (
          <Typography>{acceptedFiles[0].name}</Typography>
        ) : (
          <Typography>Drag & drop a file here, or click to select</Typography>
        )}
      </Paper>
    </Box>
  )
}
