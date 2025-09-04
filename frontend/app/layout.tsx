// "use client"
import { CssBaseline } from "@mui/material"
import type { Metadata } from "next";
export const metadata: Metadata = {
  title: "Resume Matcher",
  description: "Resume Matcher",
  icons: {
    icon: [
       { url: "/evaluation.png", type: "image/png" }, 
    ],
  },
};
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {/* <CssBaseline/> */}
        {children}</body>
    </html>
  )
}